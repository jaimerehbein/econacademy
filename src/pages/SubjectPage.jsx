import React from 'react';
import { useParams, Link } from 'react-router-dom';
import { useContent } from '../hooks/useContent';
import MarkdownRenderer from '../components/MarkdownRenderer';
import { Loader2, ArrowLeft, BarChart, Clock } from 'lucide-react';
import subjectsData from '../data.json';

const SubjectPage = () => {
    const { id } = useParams();
    const subjects = subjectsData?.asignaturas || [];
    const subject = subjects.find(s => s.codigo.toLowerCase() === id.toLowerCase());
    const { content, loading, error } = useContent(id.toLowerCase());

    if (!subject) return (
        <div className="flex flex-col items-center justify-center py-40 min-h-screen">
            <h2 className="text-3xl font-bold text-white mb-2">Asignatura no encontrada</h2>
            <p className="text-slate-400 mb-6">El módulo que buscas no existe o fue movido.</p>
            <Link to="/" className="px-6 py-2.5 bg-white/5 border border-white/10 text-slate-300 rounded-xl hover:bg-white/10 hover:text-white transition-all flex items-center gap-2">
                <ArrowLeft size={16} /> Volver al Explorador
            </Link>
        </div>
    );

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
                    {/* Header contextual breadcrumb */}
                    <div className="mb-14 flex items-center gap-3 text-[11px] font-bold text-slate-500/80 uppercase tracking-widest font-mono">
                        <span className="hover:text-slate-300 cursor-pointer transition-colors">Tech Economics</span>
                        <span className="text-slate-600">/</span>
                        <span className="hover:text-slate-300 cursor-pointer transition-colors">{subject.categoria || 'Módulo'}</span>
                        <span className="text-slate-600">/</span>
                        <span className="text-indigo-400 bg-indigo-500/10 px-2 py-0.5 rounded border border-indigo-500/20">{subject.codigo}</span>
                    </div>

                    {/* The core reading canvas */}
                    <div className="prose prose-slate prose-invert max-w-none">
                        <MarkdownRenderer content={content} />
                    </div>
                </article>
            )}
        </div>
    );
};

export default SubjectPage;
