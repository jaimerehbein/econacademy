import React from 'react';
import { X, AlignLeft, Bold, Italic, Link2, List, Save } from 'lucide-react';

const NotesPanel = ({ isOpen, onClose }) => {
    return (
        <aside
            className={`fixed top-0 right-0 h-screen w-[400px] bg-study-panel/95 backdrop-blur-3xl border-l border-white/5 shadow-[0_0_50px_rgba(0,0,0,0.5)] z-50 transform transition-transform duration-500 ease-[cubic-bezier(0.22,1,0.36,1)] ${isOpen ? 'translate-x-0' : 'translate-x-full'}`}
        >
            <div className="flex flex-col h-full">
                {/* Header */}
                <div className="px-6 py-5 border-b border-white/10 flex items-center justify-between bg-slate-900/40 relative overflow-hidden">
                    <div className="absolute top-0 right-0 w-32 h-32 bg-indigo-500/10 rounded-full blur-3xl -translate-y-1/2 translate-x-1/2"></div>
                    <div className="relative z-10">
                        <h2 className="text-xl font-bold text-slate-100 tracking-tight">Mis Apuntes</h2>
                        <p className="text-xs text-indigo-400 font-medium tracking-wide">Módulo Activo: <span className="text-white">A40</span></p>
                    </div>
                    <button
                        onClick={onClose}
                        className="p-2 text-slate-400 hover:text-white hover:bg-white/10 rounded-full transition-all duration-300 hover:rotate-90 relative z-10"
                    >
                        <X size={20} />
                    </button>
                </div>

                {/* Notes History */}
                <div className="flex-1 overflow-y-auto p-6 space-y-4 custom-scrollbar">
                    <div className="bg-slate-800/40 border text-left border-white/5 rounded-xl p-4 shadow-lg hover:shadow-xl hover:bg-slate-800/80 hover:border-white/10 transition-all duration-300 group relative overflow-hidden">
                        <div className="absolute left-0 top-0 bottom-0 w-1 bg-amber-400 shadow-[0_0_10px_rgba(251,191,36,0.5)]"></div>
                        <div className="flex justify-between items-start mb-2">
                            <h3 className="font-bold text-sm text-slate-200 group-hover:text-amber-300 transition-colors">Estructura Óptima WACC (M&M)</h3>
                            <span className="text-[10px] text-slate-500 font-mono">Hace 2 hrs</span>
                        </div>
                        <p className="text-xs text-slate-400 line-clamp-3 leading-relaxed">
                            Recordar: El teorema M&M dicta que en un mundo aséptico la estructura es irrelevante. PERO al inyectar impuestos, la deuda desplaza al equity gracias al escudo fiscal protector. ¡Vital no pasar el punto de quiebra!
                        </p>
                    </div>

                    <div className="bg-slate-800/40 border text-left border-white/5 rounded-xl p-4 shadow-lg hover:shadow-xl hover:bg-slate-800/80 hover:border-white/10 transition-all duration-300 group relative overflow-hidden">
                        <div className="absolute left-0 top-0 bottom-0 w-1 bg-emerald-400 shadow-[0_0_10px_rgba(52,211,153,0.5)]"></div>
                        <div className="flex justify-between items-start mb-2">
                            <h3 className="font-bold text-sm text-slate-200 group-hover:text-emerald-300 transition-colors">Ejemplo de Signaling</h3>
                            <span className="text-[10px] text-slate-500 font-mono">Ayer</span>
                        </div>
                        <p className="text-xs text-slate-400 line-clamp-2 leading-relaxed">
                            Bajar dividendos = Sangre en las calles para las acciones por asimetría de información.
                        </p>
                    </div>
                </div>

                {/* Editor Input Area */}
                <div className="p-5 border-t border-white/10 bg-slate-900/60 backdrop-blur-md">
                    <div className="border border-white/10 rounded-xl focus-within:ring-2 ring-indigo-500/30 focus-within:border-indigo-400 transition-all bg-slate-950/50 shadow-inner overflow-hidden">
                        {/* Editor Toolbar */}
                        <div className="flex items-center gap-1 p-2 border-b border-white/5 bg-slate-900/40">
                            <button className="p-1.5 text-slate-400 hover:text-white rounded-lg hover:bg-white/10 transition-colors"><Bold size={14} /></button>
                            <button className="p-1.5 text-slate-400 hover:text-white rounded-lg hover:bg-white/10 transition-colors"><Italic size={14} /></button>
                            <div className="w-[1px] h-4 bg-white/10 mx-1"></div>
                            <button className="p-1.5 text-slate-400 hover:text-white rounded-lg hover:bg-white/10 transition-colors"><List size={14} /></button>
                            <button className="p-1.5 text-slate-400 hover:text-white rounded-lg hover:bg-white/10 transition-colors"><AlignLeft size={14} /></button>
                            <button className="p-1.5 text-slate-400 hover:text-white rounded-lg hover:bg-white/10 transition-colors"><Link2 size={14} /></button>
                        </div>
                        <textarea
                            className="w-full bg-transparent p-4 text-sm text-slate-200 placeholder-slate-500 focus:outline-none resize-none h-32 custom-scrollbar"
                            placeholder="Escribe tus apuntes o epifanías aquí..."
                        ></textarea>
                        <div className="p-3 bg-slate-900/40 border-t border-white/5 rounded-b-xl flex justify-between items-center">
                            <span className="text-[10px] font-mono text-slate-500 flex items-center gap-1 tracking-wide">Markdown soportado</span>
                            <button className="bg-indigo-600 hover:bg-indigo-500 text-white px-5 py-2 rounded-lg text-xs font-bold flex items-center gap-1.5 transition-all duration-300 shadow-lg shadow-indigo-500/25 hover:shadow-indigo-500/40 hover:-translate-y-0.5">
                                <Save size={14} /> Guardar
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </aside>
    );
};

export default NotesPanel;
