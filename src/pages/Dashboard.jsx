import React from 'react';
import { useNavigate } from 'react-router-dom';
import { ArrowRight, BookOpen, GraduationCap, BarChart2, Cpu, Globe, TrendingUp, Layers, BookMarked } from 'lucide-react';
import subjectsData from '../data.json';

const PROGRAMS = [
    {
        key: 'Licenciatura en Economía',
        label: 'Licenciatura en Economía',
        level: 'Pregrado · 4 años',
        description: 'Fundamentos sólidos de micro y macroeconomía, econometría y economía internacional. La base de toda carrera económica.',
        Icon: GraduationCap,
        from: 'from-indigo-600', to: 'to-purple-600',
        glow: 'shadow-indigo-500/20',
        accent: 'text-indigo-300',
        accentBg: 'bg-indigo-500/10',
        accentBorder: 'border-indigo-500/20',
        dot: 'bg-indigo-400',
    },
    {
        key: 'Maestría en Ciencias Económicas',
        label: 'Maestría en Ciencias Económicas',
        level: 'Posgrado · 2 años',
        description: 'Modelos avanzados de equilibrio general, economía del bienestar y teoría de juegos aplicada a política económica.',
        Icon: BarChart2,
        from: 'from-emerald-600', to: 'to-teal-600',
        glow: 'shadow-emerald-500/20',
        accent: 'text-emerald-300',
        accentBg: 'bg-emerald-500/10',
        accentBorder: 'border-emerald-500/20',
        dot: 'bg-emerald-400',
    },
    {
        key: 'Master en Macroeconomía',
        label: 'Master en Macroeconomía',
        level: 'Especialización · 18 meses',
        description: 'Política monetaria, modelos DSGE, análisis de ciclos económicos y gestión de crisis fiscales a nivel internacional.',
        Icon: TrendingUp,
        from: 'from-fuchsia-600', to: 'to-pink-600',
        glow: 'shadow-fuchsia-500/20',
        accent: 'text-fuchsia-300',
        accentBg: 'bg-fuchsia-500/10',
        accentBorder: 'border-fuchsia-500/20',
        dot: 'bg-fuchsia-400',
    },
    {
        key: 'Master en Microeconomía',
        label: 'Master en Microeconomía',
        level: 'Especialización · 18 meses',
        description: 'Teoría del consumidor, producción, competencia imperfecta, información asimétrica y diseño de mecanismos.',
        Icon: Layers,
        from: 'from-amber-500', to: 'to-orange-500',
        glow: 'shadow-amber-500/20',
        accent: 'text-amber-300',
        accentBg: 'bg-amber-500/10',
        accentBorder: 'border-amber-500/20',
        dot: 'bg-amber-400',
    },
    {
        key: 'Master en Ingeniería Financiera',
        label: 'Master en Ingeniería Financiera',
        level: 'Especialización · 12 meses',
        description: 'Derivados, valoración de activos, riesgo de crédito, MBS, modelos estocásticos y matemáticas financieras avanzadas.',
        Icon: Cpu,
        from: 'from-cyan-600', to: 'to-blue-600',
        glow: 'shadow-cyan-500/20',
        accent: 'text-cyan-300',
        accentBg: 'bg-cyan-500/10',
        accentBorder: 'border-cyan-500/20',
        dot: 'bg-cyan-400',
    },
    {
        key: 'Master en Economía Política',
        label: 'Master en Economía Política',
        level: 'Especialización · 12 meses',
        description: 'Marxismo, imperialismo, ciclos de crisis capitalistas, economía política clásica y teoría del estado.',
        Icon: Globe,
        from: 'from-rose-600', to: 'to-red-700',
        glow: 'shadow-rose-500/20',
        accent: 'text-rose-300',
        accentBg: 'bg-rose-500/10',
        accentBorder: 'border-rose-500/20',
        dot: 'bg-rose-400',
    },
    {
        key: 'Master en Economía Básica',
        label: 'Master en Economía Básica',
        level: 'Especialización · 12 meses',
        description: 'Pensamiento económico de Thomas Sowell, mitos del mercado, precios, incentivos y consecuencias no previstas.',
        Icon: BookMarked,
        from: 'from-orange-600', to: 'to-amber-700',
        glow: 'shadow-orange-500/20',
        accent: 'text-orange-300',
        accentBg: 'bg-orange-500/10',
        accentBorder: 'border-orange-500/20',
        dot: 'bg-orange-400',
    },
];

const Dashboard = () => {
    const navigate = useNavigate();
    const subjects = subjectsData?.asignaturas || [];

    const totalModules = subjects.length;
    const totalPrograms = new Set(subjects.map(s => s.programa)).size;

    return (
        <div className="space-y-16 animate-in fade-in slide-in-from-bottom-4 duration-700">

            {/* ── Hero ── */}
            <header className="relative overflow-hidden rounded-[2.5rem] border border-white/8 bg-gradient-to-br from-slate-900 via-slate-900 to-slate-800 p-10 md:p-16 shadow-2xl">
                <div className="absolute top-0 right-0 w-[600px] h-[600px] bg-emerald-500/5 rounded-full blur-[120px] -translate-y-1/3 translate-x-1/4 pointer-events-none" />
                <div className="absolute bottom-0 left-0 w-[400px] h-[400px] bg-indigo-500/5 rounded-full blur-[100px] translate-y-1/3 -translate-x-1/4 pointer-events-none" />

                <div className="relative z-10 flex flex-col md:flex-row items-start md:items-end justify-between gap-8">
                    <div className="space-y-5 max-w-2xl">
                        <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 text-[10px] font-black tracking-[0.35em] uppercase">
                            <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse" />
                            Formación de Élite en Economía
                        </div>
                        <h1 className="text-5xl md:text-7xl font-black text-white tracking-tighter leading-none">
                            ECON<br />
                            <span className="text-transparent bg-clip-text bg-gradient-to-r from-emerald-400 to-teal-400">ACADEMY</span>
                        </h1>
                        <p className="text-slate-400 text-lg leading-relaxed font-light max-w-xl">
                            Un portal académico de élite con programas de Licenciatura, Maestría y Masters especializados en Economía, Finanzas y Política Económica.
                        </p>
                    </div>
                    <div className="flex flex-col items-end gap-2 text-right shrink-0">
                        <div className="text-5xl font-black text-white tabular-nums">{totalModules}</div>
                        <div className="text-[10px] font-bold text-slate-500 uppercase tracking-widest">Módulos disponibles</div>
                        <div className="text-2xl font-black text-slate-400 tabular-nums mt-2">{totalPrograms}</div>
                        <div className="text-[10px] font-bold text-slate-600 uppercase tracking-widest">Programas</div>
                    </div>
                </div>
            </header>

            {/* ── Program Grid ── */}
            <section className="space-y-6">
                <div className="flex items-center gap-3">
                    <div className="w-8 h-0.5 bg-emerald-500 rounded-full" />
                    <h2 className="text-slate-400 font-black text-[11px] uppercase tracking-[0.4em]">Programas Académicos</h2>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-5">
                    {PROGRAMS.map(prog => {
                        const progSubjects = subjects.filter(s => s.programa === prog.key)
                            .sort((a, b) => a.codigo.localeCompare(b.codigo, undefined, { numeric: true }));
                        const firstModule = progSubjects[0];
                        if (!progSubjects.length) return null;

                        return (
                            <div
                                key={prog.key}
                                onClick={() => firstModule && navigate(`/subject/${firstModule.codigo.toLowerCase()}`)}
                                className={`group relative overflow-hidden rounded-[1.75rem] border border-white/8 bg-white/3 hover:bg-white/6 cursor-pointer transition-all duration-300 hover:-translate-y-1 hover:shadow-xl ${prog.glow} p-7 flex flex-col gap-5`}
                            >
                                {/* Gradient ambient glow */}
                                <div className={`absolute -top-12 -right-12 w-36 h-36 rounded-full blur-3xl opacity-0 group-hover:opacity-30 transition-opacity duration-500 bg-gradient-to-br ${prog.from} ${prog.to}`} />

                                {/* Icon + Level */}
                                <div className="flex items-start justify-between">
                                    <div className={`w-12 h-12 rounded-2xl bg-gradient-to-br ${prog.from} ${prog.to} flex items-center justify-center shadow-lg flex-shrink-0 group-hover:scale-110 transition-transform duration-300`}>
                                        <prog.Icon size={22} className="text-white" />
                                    </div>
                                    <span className={`text-[9px] font-black uppercase tracking-widest ${prog.accentBg} ${prog.accentBorder} ${prog.accent} border px-2.5 py-1 rounded-full`}>
                                        {progSubjects.length} módulos
                                    </span>
                                </div>

                                {/* Text */}
                                <div className="space-y-2 flex-1">
                                    <p className={`text-[9px] font-bold uppercase tracking-widest ${prog.accent}`}>{prog.level}</p>
                                    <h3 className="text-white font-black text-lg leading-tight tracking-tight">{prog.label}</h3>
                                    <p className="text-slate-500 text-sm leading-relaxed">{prog.description}</p>
                                </div>

                                {/* Module preview tags */}
                                <div className="flex flex-wrap gap-1.5">
                                    {progSubjects.slice(0, 3).map(s => (
                                        <span key={s.codigo} className="text-[9px] font-mono font-bold text-slate-600 bg-white/5 border border-white/8 px-2 py-0.5 rounded">
                                            {s.codigo}
                                        </span>
                                    ))}
                                    {progSubjects.length > 3 && (
                                        <span className="text-[9px] font-mono font-bold text-slate-700 px-1">
                                            +{progSubjects.length - 3}
                                        </span>
                                    )}
                                </div>

                                {/* CTA */}
                                <div className={`flex items-center gap-2 ${prog.accent} text-[11px] font-black uppercase tracking-widest`}>
                                    <span>Comenzar programa</span>
                                    <ArrowRight size={12} className="group-hover:translate-x-1 transition-transform duration-300" />
                                </div>
                            </div>
                        );
                    })}
                </div>
            </section>

            {/* ── Footer tagline ── */}
            <footer className="text-center py-4 border-t border-white/5">
                <p className="text-[10px] font-bold text-slate-600 uppercase tracking-[0.4em]">
                    EconAcademy · Formación de Élite en Economía
                </p>
            </footer>
        </div>
    );
};

export default Dashboard;
