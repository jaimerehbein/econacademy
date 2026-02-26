import React from 'react';
import { useNavigate } from 'react-router-dom';
import { ArrowRight, BookOpen, GraduationCap, BarChart2, Cpu, Globe, TrendingUp, Layers, BookMarked } from 'lucide-react';
import OrbitingMasters from '../components/OrbitingMasters';
import subjectsData from '../data.json';

const PROGRAMS = [
    {
        key: 'Licenciatura en Economía',
        label: 'Licenciatura en Economía',
        level: 'Pregrado · 4 años',
        description: 'Fundamentos sólidos de micro y macroeconomía, econometría y economía internacional. La base de toda carrera económica.',
        Icon: GraduationCap,
        from: 'from-amber-600', to: 'to-orange-600',
        glow: 'shadow-amber-500/20',
        accent: 'text-amber-400',
        accentBg: 'bg-amber-500/10',
        accentBorder: 'border-amber-500/20',
        dot: 'bg-amber-400',
    },
    {
        key: 'Maestría en Ciencias Económicas',
        label: 'Maestría en Ciencias Económicas',
        level: 'Posgrado · 2 años',
        description: 'Modelos avanzados de equilibrio general, economía del bienestar y teoría de juegos aplicada a política económica.',
        Icon: BarChart2,
        from: 'from-orange-500', to: 'to-amber-600',
        glow: 'shadow-orange-500/20',
        accent: 'text-orange-400',
        accentBg: 'bg-orange-500/10',
        accentBorder: 'border-orange-500/20',
        dot: 'bg-orange-400',
    },
    {
        key: 'Master en Macroeconomía',
        label: 'Master en Macroeconomía',
        level: 'Especialización · 18 meses',
        description: 'Política monetaria, modelos DSGE, análisis de ciclos económicos y gestión de crisis fiscales a nivel internacional.',
        Icon: TrendingUp,
        from: 'from-amber-500', to: 'to-orange-500',
        glow: 'shadow-amber-500/20',
        accent: 'text-amber-300',
        accentBg: 'bg-amber-500/10',
        accentBorder: 'border-amber-500/20',
        dot: 'bg-amber-400',
    },
    {
        key: 'Master en Microeconomía',
        label: 'Master en Microeconomía',
        level: 'Especialización · 18 meses',
        description: 'Teoría del consumidor, producción, competencia imperfecta, información asimétrica y diseño de mecanismos.',
        Icon: Layers,
        from: 'from-orange-600', to: 'to-amber-700',
        glow: 'shadow-orange-500/20',
        accent: 'text-orange-300',
        accentBg: 'bg-orange-500/10',
        accentBorder: 'border-orange-500/20',
        dot: 'bg-orange-400',
    },
    {
        key: 'Master en Ingeniería Financiera',
        label: 'Master en Ingeniería Financiera',
        level: 'Especialización · 12 meses',
        description: 'Derivados, valoración de activos, riesgo de crédito, MBS, modelos estocásticos y matemáticas financieras avanzadas.',
        Icon: Cpu,
        from: 'from-amber-600', to: 'to-orange-700',
        glow: 'shadow-amber-500/20',
        accent: 'text-amber-200',
        accentBg: 'bg-amber-500/10',
        accentBorder: 'border-amber-500/20',
        dot: 'bg-amber-400',
    },
    {
        key: 'Master en Economía Política',
        label: 'Master en Economía Política',
        level: 'Especialización · 12 meses',
        description: 'Marxismo, imperialismo, ciclos de crisis capitalistas, economía política clásica y teoría del estado.',
        Icon: BookOpen,
        from: 'from-orange-700', to: 'to-slate-800',
        glow: 'shadow-orange-500/20',
        accent: 'text-orange-300',
        accentBg: 'bg-orange-500/10',
        accentBorder: 'border-orange-500/20',
        dot: 'bg-orange-400',
    },
    {
        key: 'Master en Economía Básica',
        label: 'Master en Economía Básica',
        level: 'Especialización · 12 meses',
        description: 'Pensamiento económico de Thomas Sowell, mitos del mercado, precios, incentivos y consecuencias no previstas.',
        Icon: BookMarked,
        from: 'from-amber-400', to: 'to-orange-500',
        glow: 'shadow-amber-400/20',
        accent: 'text-amber-100',
        accentBg: 'bg-amber-500/10',
        accentBorder: 'border-amber-500/20',
        dot: 'bg-amber-300',
    },
    {
        key: 'Master en Economía Internacional',
        label: 'Master en Economía Internacional',
        level: 'Especialización · 12 meses',
        description: 'Comercio global, política arancelaria, tipos de cambio, macrosistema abierto y crisis financieras.',
        Icon: Globe,
        from: 'from-orange-500', to: 'to-amber-500',
        glow: 'shadow-orange-500/20',
        accent: 'text-orange-200',
        accentBg: 'bg-orange-500/10',
        accentBorder: 'border-orange-500/20',
        dot: 'bg-orange-400',
    },
    {
        key: 'Master en Matemáticas Económicas',
        label: 'Master en Matemáticas Económicas',
        level: 'Cuantitativo · 12 meses',
        description: 'Cálculo diferencial avanzado, álgebra de Leontief, optimización multivariable estática y dinámica.',
        Icon: TrendingUp,
        from: 'from-amber-600', to: 'to-accent-success',
        glow: 'shadow-accent-success/20',
        accent: 'text-accent-success',
        accentBg: 'bg-accent-success/10',
        accentBorder: 'border-accent-success/20',
        dot: 'bg-accent-success',
    },
    {
        key: 'Compendio Visual de Modelos',
        label: 'Modeloteca Global',
        level: 'Visual · Infinito',
        description: 'La cartografía definitiva del pensamiento académico. Modelos destilados en topologías de red neuronales (Mindmaps).',
        Icon: Layers,
        from: 'from-accent-success', to: 'to-emerald-700',
        glow: 'shadow-accent-success/30',
        accent: 'text-accent-success',
        accentBg: 'bg-accent-success/10',
        accentBorder: 'border-accent-success/20',
        dot: 'bg-accent-success',
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
            <header className="relative overflow-hidden rounded-3xl md:rounded-[3rem] border border-white/10 bg-[#06080f] p-6 md:p-20 shadow-[0_32px_64px_-16px_rgba(0,0,0,0.6)]">
                {/* Patagon-style Ambient Glows */}
                <div className="absolute top-0 right-0 w-[800px] h-[800px] bg-amber-600/10 rounded-full blur-[140px] -translate-y-1/2 translate-x-1/4 pointer-events-none" />
                <div className="absolute bottom-0 left-0 w-[600px] h-[600px] bg-orange-600/5 rounded-full blur-[120px] translate-y-1/2 -translate-x-1/4 pointer-events-none" />
                <div className="absolute inset-0 bg-[url('https://www.transparenttextures.com/patterns/carbon-fibre.png')] opacity-[0.03] pointer-events-none mix-blend-overlay" />

                <div className="relative z-10 flex flex-col xl:flex-row items-center justify-between gap-12 py-10 xl:py-4">
                    <div className="space-y-8 max-w-3xl text-center xl:text-left z-20">
                        <div className="inline-flex items-center gap-2.5 px-5 py-2 rounded-full bg-amber-500/10 border border-amber-500/20 text-amber-500 text-[10px] font-black tracking-[0.4em] uppercase shadow-lg">
                            <span className="w-2 h-2 rounded-full bg-amber-500 animate-[pulse_2s_infinite]" />
                            Formación de Élite en Economía
                        </div>
                        <h1 className="text-5xl md:text-7xl lg:text-8xl font-black text-white tracking-tight leading-[0.95] drop-shadow-2xl max-w-2xl mx-auto xl:mx-0">
                            ECON<br />
                            <span className="text-transparent bg-clip-text bg-gradient-to-r from-amber-400 via-orange-500 to-amber-600">ACADEMY</span>
                        </h1>
                        <p className="text-slate-400 text-base md:text-xl leading-relaxed font-light max-w-xl mx-auto xl:mx-0 md:border-l-2 md:border-amber-500/30 md:pl-6 py-2">
                            La plataforma definitiva para el dominio técnico de modelos económicos. Programas de <span className="text-white font-medium">Postgrado de alto rendimiento</span> diseñados para la élite intelectual.
                        </p>

                        <div className="flex flex-wrap items-center justify-center xl:justify-start gap-4 pt-4">
                            <button className="px-8 py-4 bg-amber-500 hover:bg-amber-400 text-black font-black text-xs uppercase tracking-widest rounded-2xl transition-all duration-300 transform hover:scale-105 hover:shadow-[0_0_30px_rgba(245,158,11,0.4)] active:scale-95">
                                Comenzar Ahora
                            </button>
                            <button className="px-8 py-4 bg-white/5 hover:bg-white/10 backdrop-blur-xl border border-white/10 text-white font-black text-xs uppercase tracking-widest rounded-2xl transition-all duration-300">
                                Explorar Programas
                            </button>
                        </div>
                    </div>
                    <div className="flex-shrink-0 z-10 -mt-10 md:mt-0 xl:my-0 scale-[0.7] sm:scale-90 md:scale-100 lg:scale-110 xl:scale-125 xl:mr-10 xl:ml-auto transition-all duration-700">
                        <OrbitingMasters />
                    </div>
                </div>
            </header>

            {/* ── Program Grid ── */}
            <section className="space-y-10">
                <div className="flex flex-col md:flex-row md:items-end justify-between gap-4">
                    <div className="space-y-2">
                        <div className="flex items-center gap-3">
                            <div className="w-12 h-1 bg-amber-500 rounded-full" />
                            <h2 className="text-amber-500/80 font-black text-[11px] uppercase tracking-[0.5em]">Catálogo de Élite</h2>
                        </div>
                        <h3 className="text-3xl md:text-5xl font-black text-white tracking-tight">Nuestros Programas</h3>
                    </div>
                    <p className="text-slate-500 max-w-md text-sm leading-relaxed">
                        Explora nuestra selección rigurosa de especializaciones diseñadas para arquitectos del sistema financiero y analistas de política global.
                    </p>
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
