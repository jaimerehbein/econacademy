import React from 'react';
import { useParams, Link, useNavigate } from 'react-router-dom';
import { useContent } from '../hooks/useContent';
import MarkdownRenderer from '../components/MarkdownRenderer';
import { Loader2, ArrowLeft, ArrowRight, ChevronRight, BookOpen, LayoutGrid } from 'lucide-react';
import subjectsData from '../data.json';

// Color map for program badges
const PROGRAM_COLORS = {
    'Licenciatura en Economía': { accent: 'text-indigo-400', bg: 'bg-indigo-500/10', border: 'border-indigo-500/25' },
    'Maestría en Ciencias Económicas': { accent: 'text-emerald-400', bg: 'bg-emerald-500/10', border: 'border-emerald-500/25' },
    'Master en Macroeconomía': { accent: 'text-fuchsia-400', bg: 'bg-fuchsia-500/10', border: 'border-fuchsia-500/25' },
    'Master en Microeconomía': { accent: 'text-amber-400', bg: 'bg-amber-500/10', border: 'border-amber-500/25' },
    'Master en Ingeniería Financiera': { accent: 'text-cyan-400', bg: 'bg-cyan-500/10', border: 'border-cyan-500/25' },
    'Master en Economía Política': { accent: 'text-rose-400', bg: 'bg-rose-500/10', border: 'border-rose-500/25' },
    'Master en Economía Básica': { accent: 'text-orange-400', bg: 'bg-orange-500/10', border: 'border-orange-500/25' },
};

const DEFAULT_COLOR = { accent: 'text-slate-400', bg: 'bg-slate-500/10', border: 'border-slate-500/25' };

const SubjectPage = () => {
    const { id } = useParams();
    const navigate = useNavigate();
    const subjects = subjectsData?.asignaturas || [];
    const subject = subjects.find(s => s.codigo.toLowerCase() === id.toLowerCase());
    const { content, loading, error } = useContent(id.toLowerCase());

    // Get siblings — same program, sorted by código
    const siblings = subjects
        .filter(s => s.programa === subject?.programa)
        .sort((a, b) => a.codigo.localeCompare(b.codigo, undefined, { numeric: true }));

    const currentIndex = siblings.findIndex(s => s.codigo.toLowerCase() === id.toLowerCase());
    const prevSubject = currentIndex > 0 ? siblings[currentIndex - 1] : null;
    const nextSubject = currentIndex < siblings.length - 1 ? siblings[currentIndex + 1] : null;

    const colors = PROGRAM_COLORS[subject?.programa] || DEFAULT_COLOR;

    if (!subject) return (
        <div className="flex flex-col items-center justify-center py-40 min-h-screen">
            <h2 className="text-3xl font-bold text-white mb-2">Asignatura no encontrada</h2>
            <p className="text-slate-400 mb-6">El módulo que buscas no existe o fue movido.</p>
            <Link to="/" className="px-6 py-2.5 bg-white/5 border border-white/10 text-slate-300 rounded-xl hover:bg-white/10 hover:text-white transition-all flex items-center gap-2">
                <ArrowLeft size={16} /> Volver al Explorador
            </Link>
        </div>
    );

    const progressPct = siblings.length > 1 ? Math.round(((currentIndex + 1) / siblings.length) * 100) : 100;

    return (
        <div className="animate-in fade-in slide-in-from-bottom-8 duration-700 min-h-screen">
            {loading ? (
                <div className="flex flex-col items-center justify-center py-40 space-y-6">
                    <div className="relative">
                        <div className="absolute inset-0 bg-indigo-500 blur-xl opacity-20 rounded-full animate-pulse"></div>
                        <Loader2 size={48} className="text-indigo-400 animate-spin relative z-10" />
                    </div>
                    <p className="text-indigo-300/80 font-bold font-mono text-[11px] uppercase tracking-[0.4em] animate-pulse">
                        Descifrando Conocimiento...
                    </p>
                </div>
            ) : error ? (
                <div className="bg-red-500/10 backdrop-blur-md border-l-4 border-red-500/50 p-8 rounded-xl shadow-lg shadow-red-500/5 my-10">
                    <p className="text-red-400 font-bold uppercase tracking-widest text-sm flex items-center gap-2">
                        <span className="w-2 h-2 rounded-full bg-red-500 animate-ping"></span>
                        Anomalía Detectada
                    </p>
                    <p className="text-red-200/80 mt-3 text-sm leading-relaxed">{error}</p>
                </div>
            ) : (
                <article className="max-w-4xl mx-auto bg-transparent relative z-10">

                    {/* ── Breadcrumb ── */}
                    <div className="mb-8 flex items-center gap-2 text-[11px] font-bold text-slate-500 uppercase tracking-widest font-mono flex-wrap">
                        <Link to="/" className="hover:text-slate-300 transition-colors flex items-center gap-1">
                            <LayoutGrid size={10} /> EconAcademy
                        </Link>
                        <ChevronRight size={10} className="text-slate-700" />
                        <span className={`${colors.accent} ${colors.bg} ${colors.border} border px-2 py-0.5 rounded`}>
                            {subject.programa}
                        </span>
                        <ChevronRight size={10} className="text-slate-700" />
                        <span className="text-slate-400">{subject.nombre}</span>
                    </div>

                    {/* ── Progress bar within program ── */}
                    {siblings.length > 1 && (
                        <div className="mb-10">
                            <div className="flex items-center justify-between mb-2">
                                <span className="text-[10px] font-mono font-bold text-slate-500 uppercase tracking-widest">
                                    Módulo {currentIndex + 1} de {siblings.length}
                                </span>
                                <span className={`text-[10px] font-mono font-black ${colors.accent}`}>{progressPct}%</span>
                            </div>
                            <div className="w-full h-0.5 bg-white/5 rounded-full overflow-hidden">
                                <div
                                    className={`h-full rounded-full transition-all duration-700 ${colors.bg.replace('bg-', 'bg-').replace('/10', '')} ${colors.accent.replace('text-', 'bg-')}`}
                                    style={{ width: `${progressPct}%` }}
                                />
                            </div>
                        </div>
                    )}

                    {/* ── Content ── */}
                    <div className="prose prose-slate prose-invert max-w-none">
                        <MarkdownRenderer content={content} />
                    </div>

                    {/* ── Prev / Next navigation ── */}
                    <nav className="mt-20 pt-8 border-t border-white/5 grid grid-cols-1 sm:grid-cols-2 gap-4">
                        {prevSubject ? (
                            <button
                                onClick={() => navigate(`/subject/${prevSubject.codigo.toLowerCase()}`)}
                                className="group flex flex-col gap-1.5 p-5 bg-white/3 hover:bg-white/8 border border-white/8 hover:border-white/15 rounded-2xl transition-all duration-300 text-left hover:-translate-y-0.5"
                            >
                                <span className="flex items-center gap-1.5 text-[10px] font-mono font-bold text-slate-600 uppercase tracking-widest">
                                    <ArrowLeft size={10} className="group-hover:-translate-x-1 transition-transform" />
                                    Módulo anterior
                                </span>
                                <span className="text-sm font-bold text-slate-300 group-hover:text-white transition-colors leading-snug">
                                    {prevSubject.nombre}
                                </span>
                                <span className={`text-[10px] font-mono ${colors.accent}`}>{prevSubject.codigo}</span>
                            </button>
                        ) : <div />}

                        {nextSubject ? (
                            <button
                                onClick={() => navigate(`/subject/${nextSubject.codigo.toLowerCase()}`)}
                                className="group flex flex-col gap-1.5 p-5 bg-white/3 hover:bg-white/8 border border-white/8 hover:border-white/15 rounded-2xl transition-all duration-300 text-right sm:items-end hover:-translate-y-0.5"
                            >
                                <span className="flex items-center gap-1.5 text-[10px] font-mono font-bold text-slate-600 uppercase tracking-widest">
                                    Siguiente módulo
                                    <ArrowRight size={10} className="group-hover:translate-x-1 transition-transform" />
                                </span>
                                <span className="text-sm font-bold text-slate-300 group-hover:text-white transition-colors leading-snug">
                                    {nextSubject.nombre}
                                </span>
                                <span className={`text-[10px] font-mono ${colors.accent}`}>{nextSubject.codigo}</span>
                            </button>
                        ) : (
                            <div className="flex flex-col gap-1.5 p-5 bg-emerald-500/5 border border-emerald-500/15 rounded-2xl text-right sm:items-end">
                                <span className="text-[10px] font-mono font-bold text-emerald-500/60 uppercase tracking-widest">
                                    ✓ Programa completado
                                </span>
                                <Link to="/" className="text-sm font-bold text-emerald-400 hover:text-emerald-300 transition-colors">
                                    Explorar otros programas →
                                </Link>
                            </div>
                        )}
                    </nav>
                </article>
            )}
        </div>
    );
};

export default SubjectPage;
