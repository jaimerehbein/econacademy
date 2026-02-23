import React, { useState } from 'react';
import { NavLink } from 'react-router-dom';
import { ChevronRight, GraduationCap, Home, LayoutList, Hash, BookMarked, ChevronDown } from 'lucide-react';
import subjectsData from '../data.json';

// Program definitions (display config)
const PROGRAMS = [
    {
        key: 'Licenciatura en Economía',
        label: 'Licenciatura',
        sublabel: 'en Economía',
        badge: 'LIC',
        color: 'indigo',
        from: 'from-indigo-500',
        to: 'to-purple-500',
        accent: 'text-indigo-300',
        accentBg: 'bg-indigo-500/15',
        accentBorder: 'border-indigo-500/25',
        barColor: 'bg-indigo-500',
        hasSortToggle: true,
    },
    {
        key: 'Maestría en Ciencias Económicas',
        label: 'Maestría',
        sublabel: 'en Ciencias Económicas',
        badge: 'MCE',
        color: 'emerald',
        from: 'from-emerald-500',
        to: 'to-teal-500',
        accent: 'text-emerald-300',
        accentBg: 'bg-emerald-500/15',
        accentBorder: 'border-emerald-500/25',
        barColor: 'bg-emerald-500',
        hasSortToggle: false,
    },
    {
        key: 'Master en Macroeconomía',
        label: 'Master',
        sublabel: 'en Macroeconomía',
        badge: 'MAC',
        color: 'fuchsia',
        from: 'from-fuchsia-500',
        to: 'to-pink-500',
        accent: 'text-fuchsia-300',
        accentBg: 'bg-fuchsia-500/15',
        accentBorder: 'border-fuchsia-500/25',
        barColor: 'bg-fuchsia-500',
        hasSortToggle: false,
    },
    {
        key: 'Master en Microeconomía',
        label: 'Master',
        sublabel: 'en Microeconomía',
        badge: 'MIC',
        color: 'amber',
        from: 'from-amber-500',
        to: 'to-orange-500',
        accent: 'text-amber-300',
        accentBg: 'bg-amber-500/15',
        accentBorder: 'border-amber-500/25',
        barColor: 'bg-amber-500',
        hasSortToggle: false,
    },
    {
        key: 'Sowell Master Series',
        label: 'Sowell',
        sublabel: 'Master Series',
        badge: 'SOW',
        color: 'orange',
        from: 'from-orange-500',
        to: 'to-amber-600',
        accent: 'text-orange-300',
        accentBg: 'bg-orange-500/15',
        accentBorder: 'border-orange-500/25',
        barColor: 'bg-orange-500',
        hasSortToggle: false,
    },
    {
        key: 'Master en Ingeniería Financiera',
        label: 'Master',
        sublabel: 'Ingeniería Financiera',
        badge: 'IF',
        color: 'emerald',
        from: 'from-emerald-600',
        to: 'to-indigo-600',
        accent: 'text-emerald-300',
        accentBg: 'bg-emerald-500/15',
        accentBorder: 'border-emerald-500/25',
        barColor: 'bg-emerald-500',
        hasSortToggle: false,
    },
    {
        key: 'Master en Pensamiento Económico',
        label: 'Master',
        sublabel: 'Pensamiento Económico',
        badge: 'PE',
        color: 'stone',
        from: 'from-stone-600',
        to: 'to-stone-800',
        accent: 'text-stone-300',
        accentBg: 'bg-stone-500/15',
        accentBorder: 'border-stone-500/25',
        barColor: 'bg-stone-500',
        hasSortToggle: false,
    },
    {
        key: 'Master en Modelos Económicos',
        label: 'Master',
        sublabel: 'Modelos Económicos',
        badge: 'ME',
        color: 'violet',
        from: 'from-violet-600',
        to: 'to-cyan-600',
        accent: 'text-violet-300',
        accentBg: 'bg-violet-500/15',
        accentBorder: 'border-violet-500/25',
        barColor: 'bg-violet-500',
        hasSortToggle: false,
    },
    {
        key: 'Master en Economía Política',
        label: 'Master',
        sublabel: 'Economía Política',
        badge: 'EP',
        color: 'rose',
        from: 'from-rose-600',
        to: 'to-slate-800',
        accent: 'text-rose-300',
        accentBg: 'bg-rose-500/15',
        accentBorder: 'border-rose-500/25',
        barColor: 'bg-rose-500',
        hasSortToggle: false,
    },
];

function sortByProgramNumber(subjects) {
    return [...subjects].sort((a, b) => {
        const numA = parseInt((a.codigo || '').replace(/\D/g, ''), 10) || 0;
        const numB = parseInt((b.codigo || '').replace(/\D/g, ''), 10) || 0;
        return numA - numB;
    });
}

const SubjectLink = ({ sub, onClick }) => (
    <NavLink to={`/subject/${sub.codigo.toLowerCase()}`} className="block" onClick={onClick}>
        {({ isActive }) => (
            <div className={`
                group flex items-center justify-between px-4 py-2.5 rounded-lg text-sm transition-all duration-300 border
                ${isActive
                    ? 'bg-gradient-to-r from-indigo-600/90 to-purple-600/90 text-white shadow-lg shadow-indigo-500/25 border-white/10 translate-x-1'
                    : 'border-transparent hover:bg-white/5 hover:text-slate-100 hover:translate-x-1'}
            `}>
                <div className="flex items-center gap-3 overflow-hidden">
                    <span className={`text-[10px] font-mono font-bold px-1.5 py-0.5 rounded transition-colors ${isActive ? 'bg-white/20 text-white' : 'bg-slate-800/80 text-slate-500 group-hover:bg-slate-700/80 group-hover:text-slate-300'}`}>
                        {sub.codigo}
                    </span>
                    <span className="truncate font-medium tracking-wide">{sub.nombre}</span>
                </div>
                <ChevronRight size={14} className={`transition-all duration-300 ${isActive ? 'rotate-90 opacity-100 text-white' : 'opacity-0 -translate-x-2 group-hover:opacity-100 group-hover:translate-x-0 text-slate-400'}`} />
            </div>
        )}
    </NavLink>
);

const ProgramBlock = ({ prog, subjects, onLinkClick }) => {
    const [open, setOpen] = useState(true);
    const [viewMode, setViewMode] = useState('category');

    const categories = subjects.reduce((acc, sub) => {
        // Strip "Maestría · " or "Master · " prefix for cleaner category labels
        const cat = (sub.categoria || 'General').replace(/^(?:Maestría|Master)\s*·\s*/i, '');
        if (!acc[cat]) acc[cat] = [];
        acc[cat].push(sub);
        return acc;
    }, {});

    const sortedFlat = sortByProgramNumber(subjects);

    return (
        <div className="mb-4">
            {/* Program header */}
            <button
                onClick={() => setOpen(o => !o)}
                className={`w-full flex items-center justify-between px-3 py-2 rounded-xl mb-2 transition-all duration-200 ${prog.accentBg} border ${prog.accentBorder} hover:brightness-110`}
            >
                <div className="flex items-center gap-2.5">
                    <div className={`bg-gradient-to-br ${prog.from} ${prog.to} w-6 h-6 rounded-md flex items-center justify-center flex-shrink-0`}>
                        <span className="text-[9px] font-black text-white">{prog.badge}</span>
                    </div>
                    <div className="text-left">
                        <p className={`text-[11px] font-black ${prog.accent} leading-none`}>{prog.label}</p>
                        <p className="text-[9px] text-slate-500 leading-none mt-0.5 truncate max-w-[160px]">{prog.sublabel}</p>
                    </div>
                </div>
                <div className="flex items-center gap-2">
                    <span className="text-[9px] text-slate-600 font-mono">{subjects.length}</span>
                    <ChevronDown size={12} className={`text-slate-500 transition-transform duration-200 ${open ? 'rotate-180' : ''}`} />
                </div>
            </button>

            {open && (
                <div className="ml-1 space-y-2">
                    {/* Sort toggle — only for Licenciatura */}
                    {prog.hasSortToggle && (
                        <div className="flex items-center gap-1.5 mb-3">
                            <button
                                onClick={() => setViewMode('category')}
                                className={`flex-1 flex items-center justify-center gap-1 py-1 rounded-lg text-[9px] font-black uppercase tracking-widest transition-all ${viewMode === 'category' ? `${prog.accentBg} ${prog.accent} border ${prog.accentBorder}` : 'text-slate-600 hover:text-slate-400'}`}
                            >
                                <LayoutList size={9} />Área
                            </button>
                            <button
                                onClick={() => setViewMode('program')}
                                className={`flex-1 flex items-center justify-center gap-1 py-1 rounded-lg text-[9px] font-black uppercase tracking-widest transition-all ${viewMode === 'program' ? `${prog.accentBg} ${prog.accent} border ${prog.accentBorder}` : 'text-slate-600 hover:text-slate-400'}`}
                            >
                                <Hash size={9} />Orden
                            </button>
                        </div>
                    )}

                    {/* Category view */}
                    {viewMode === 'category' && Object.entries(categories).map(([cat, items]) => (
                        <div key={cat} className="space-y-1">
                            {Object.keys(categories).length > 1 && (
                                <h4 className={`px-4 text-[9px] font-extrabold ${prog.accent} uppercase tracking-[0.2em] mb-1`}>{cat}</h4>
                            )}
                            {items.map(sub => <SubjectLink key={sub.id} sub={sub} onClick={onLinkClick} />)}
                        </div>
                    ))}

                    {/* Program number view (only Licenciatura has toggle) */}
                    {viewMode === 'program' && (
                        <div className="space-y-1">
                            {sortedFlat.map(sub => <SubjectLink key={sub.id} sub={sub} onClick={onLinkClick} />)}
                        </div>
                    )}
                </div>
            )}

            {/* Divider */}
            <div className="mt-4 h-px bg-white/5" />
        </div>
    );
};

const Sidebar = ({ isOpen, setIsOpen }) => {
    const subjects = subjectsData?.asignaturas || [];

    // Group by programa
    const byProgram = subjects.reduce((acc, sub) => {
        const prog = sub.programa || 'Licenciatura en Economía';
        if (!acc[prog]) acc[prog] = [];
        acc[prog].push(sub);
        return acc;
    }, {});

    const handleLinkClick = () => {
        if (window.innerWidth < 1024) {
            setIsOpen(false);
        }
    };

    return (
        <aside className={`w-80 h-screen bg-study-panel/95 backdrop-blur-3xl text-slate-300 flex flex-col fixed left-0 top-0 z-50 border-r border-white/5 overflow-hidden shadow-2xl transition-transform duration-300 ease-in-out ${isOpen ? 'translate-x-0' : '-translate-x-full lg:translate-x-0'}`}>
            {/* Logo */}
            <div className="p-4 md:p-6 border-b border-white/5 flex items-center justify-between gap-4 relative overflow-hidden flex-shrink-0">
                <div className="flex items-center">
                    <div className="absolute top-0 left-0 w-full h-full bg-gradient-to-b from-emerald-500/5 to-transparent pointer-events-none" />
                    <img
                        src="/assets/logo.png"
                        alt="EconAcademy"
                        className="relative z-10 h-16 w-auto object-contain drop-shadow-lg"
                    />
                </div>
                <button
                    onClick={() => setIsOpen(false)}
                    className="lg:hidden p-2 text-slate-400 hover:text-white hover:bg-white/5 rounded-lg transition-colors absolute right-2 top-4 z-20"
                >
                    ✕
                </button>
            </div>

            <nav className="flex-1 overflow-y-auto p-4 scroll-smooth pb-10 custom-scrollbar">
                {/* Home link */}
                <div className="mb-5">
                    <NavLink
                        to="/"
                        onClick={handleLinkClick}
                        className={({ isActive }) =>
                            `flex items-center gap-3 px-4 py-3 rounded-xl transition-all duration-300 ${isActive
                                ? 'bg-white/10 text-indigo-300 font-semibold border border-white/10 shadow-[inset_0_1px_0_rgba(255,255,255,0.1)]'
                                : 'hover:bg-white/5 hover:text-white text-slate-400'
                            }`
                        }
                    >
                        {({ isActive }) => (
                            <>
                                <Home size={18} className={isActive ? 'text-indigo-400' : ''} />
                                <span className="text-sm tracking-wide">Explorador General</span>
                            </>
                        )}
                    </NavLink>
                </div>

                {/* Program blocks in defined order */}
                {PROGRAMS.map(prog => {
                    const items = byProgram[prog.key] || [];
                    if (!items.length) return null;
                    return <ProgramBlock key={prog.key} prog={prog} subjects={items} onLinkClick={handleLinkClick} />;
                })}
            </nav>

            {/* Footer */}
            <div className="p-5 border-t border-white/5 bg-slate-900/60 backdrop-blur-md flex-shrink-0">
                <div className="flex items-center justify-between mb-2">
                    <span className="text-[10px] font-bold text-slate-300 uppercase tracking-widest">Sincronización</span>
                    <div className="relative flex h-2.5 w-2.5">
                        <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                        <span className="relative inline-flex rounded-full h-2.5 w-2.5 bg-emerald-500"></span>
                    </div>
                </div>
                <p className="text-[11px] text-slate-400 flex items-center gap-1.5">
                    <span className="w-1.5 h-1.5 rounded-full bg-slate-500"></span>
                    3 programas · <span className="text-white font-medium">{subjects.length} módulos</span>
                </p>
            </div>
        </aside>
    );
};

export default Sidebar;
