import React from 'react';
import { BookOpen, GraduationCap, TrendingUp, Users } from 'lucide-react';
import subjectsData from '../data.json';

const Dashboard = () => {
    const stats = [
        { label: 'Asignaturas Totales', value: subjectsData.asignaturas.length, icon: BookOpen, color: 'text-indigo-400', bg: 'bg-indigo-500/20', border: 'border-indigo-500/30' },
        { label: 'Créditos Estimados', value: subjectsData.asignaturas.length * 6, icon: GraduationCap, color: 'text-emerald-400', bg: 'bg-emerald-500/20', border: 'border-emerald-500/30' },
        { label: 'Categorías Académicas', value: new Set(subjectsData.asignaturas.map(s => s.categoria)).size, icon: TrendingUp, color: 'text-cyan-400', bg: 'bg-cyan-500/20', border: 'border-cyan-500/30' },
        { label: 'Perfil de Egresado', value: 'Economista Global', icon: Users, color: 'text-purple-400', bg: 'bg-purple-500/20', border: 'border-purple-500/30' },
    ];

    return (
        <div className="space-y-12 animate-in fade-in slide-in-from-bottom-4 duration-700">
            <header className="space-y-4">
                <h2 className="text-4xl md:text-5xl font-extrabold text-white tracking-tight">Bienvenido al Portal de Licenciatura</h2>
                <p className="text-lg text-slate-300 max-w-3xl leading-relaxed">
                    Explora el currículo completo de Economía. Cada programa ha sido diseñado con estándares internacionales y un enfoque en análisis cuantitativo avanzado y estrategia global.
                </p>
            </header>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                {stats.map((stat) => (
                    <div key={stat.label} className="glass-panel p-6 rounded-3xl hover:-translate-y-1 transition-all duration-300 group relative overflow-hidden">
                        {/* Ambient glow effect inside card */}
                        <div className={`absolute -top-10 -right-10 w-32 h-32 rounded-full blur-3xl opacity-20 transition-opacity duration-500 group-hover:opacity-40 ${stat.bg.replace('/20', '')}`}></div>

                        <div className={`${stat.bg} ${stat.color} ${stat.border} border w-12 h-12 rounded-2xl flex items-center justify-center mb-5 group-hover:scale-110 group-hover:rotate-3 transition-transform duration-300 shadow-lg`}>
                            <stat.icon size={24} />
                        </div>
                        <p className="text-sm font-semibold text-slate-300 tracking-wide uppercase">{stat.label}</p>
                        <p className={`text-2xl font-bold text-white mt-1 group-hover:${stat.color} transition-colors duration-300`}>{stat.value}</p>
                    </div>
                ))}
            </div>

            <section className="bg-gradient-to-br from-indigo-900 via-purple-900 to-slate-900 rounded-[2.5rem] p-12 text-white shadow-[0_0_50px_rgba(79,70,229,0.2)] border border-white/10 relative overflow-hidden group">
                {/* Animated Background Elements */}
                <div className="absolute top-0 right-0 w-[500px] h-[500px] bg-indigo-500/20 rounded-full blur-[100px] -translate-y-1/2 translate-x-1/3 group-hover:scale-110 transition-transform duration-700"></div>
                <div className="absolute bottom-0 left-0 w-[300px] h-[300px] bg-purple-500/20 rounded-full blur-[80px] translate-y-1/3 -translate-x-1/4 group-hover:scale-110 transition-transform duration-700"></div>

                <div className="relative z-10 flex flex-col md:flex-row justify-between items-center gap-12">
                    <div className="space-y-6 max-w-xl">
                        <div className="inline-block px-4 py-1.5 rounded-full bg-indigo-500/20 border border-indigo-500/30 text-indigo-300 text-xs font-bold tracking-widest uppercase mb-2 shadow-[0_0_15px_rgba(99,102,241,0.2)]">
                            Visión 2026
                        </div>
                        <h3 className="text-4xl md:text-5xl font-extrabold tracking-tight text-transparent bg-clip-text bg-gradient-to-r from-white to-slate-400">
                            Plan de Estudios
                        </h3>
                        <p className="text-slate-300 text-lg leading-relaxed font-light">
                            Nuestro programa integra las últimas tendencias en Econometría, Inteligencia Artificial aplicada a la economía y Gestión de Riesgos Globales. Haz clic en el menú lateral para sumergirte en cualquier asignatura.
                        </p>
                        <div className="flex flex-wrap gap-4 pt-4">
                            <span className="px-5 py-2.5 bg-white/5 backdrop-blur-md rounded-xl text-sm font-semibold border border-white/10 shadow-lg text-slate-200 hover:bg-white/10 transition-colors cursor-pointer flex items-center gap-2">
                                <span className="w-2 h-2 rounded-full bg-cyan-400 animate-pulse"></span>
                                Economía Abierta
                            </span>
                            <span className="px-5 py-2.5 bg-white/5 backdrop-blur-md rounded-xl text-sm font-semibold border border-white/10 shadow-lg text-slate-200 hover:bg-white/10 transition-colors cursor-pointer flex items-center gap-2">
                                <span className="w-2 h-2 rounded-full bg-purple-400 animate-pulse"></span>
                                Análisis Cuantitativo
                            </span>
                        </div>
                    </div>
                    <div className="w-full md:w-auto relative hidden md:block">
                        <div className="w-64 h-64 border border-white/10 rounded-full flex items-center justify-center relative bg-white/5 backdrop-blur-sm shadow-2xl">
                            <div className="w-48 h-48 border border-white/20 rounded-full border-dashed animate-[spin_20s_linear_infinite] flex items-center justify-center">
                                <div className="w-32 h-32 bg-gradient-to-tr from-indigo-500 to-purple-500 rounded-full shadow-[0_0_40px_rgba(99,102,241,0.5)] flex items-center justify-center animate-pulse">
                                    <BookOpen size={40} className="text-white" />
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        </div>
    );
};

export default Dashboard;
