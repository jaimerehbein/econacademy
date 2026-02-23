import React from 'react';
import { PenLine } from 'lucide-react';

const FloatingTools = ({ onOpenNotes }) => {
    return (
        <div className="fixed right-6 top-1/2 -translate-y-1/2 flex flex-col gap-3 z-50">
            <button
                onClick={onOpenNotes}
                className="group relative w-12 h-12 bg-slate-900/80 backdrop-blur-md border border-white/10 rounded-full flex items-center justify-center text-slate-400 hover:text-indigo-400 hover:border-indigo-400/50 shadow-lg hover:shadow-indigo-500/20 transition-all duration-300 hover:scale-110"
                aria-label="Mis Apuntes"
            >
                <PenLine size={20} />
                <span className="absolute right-full mr-4 bg-slate-900/90 backdrop-blur-xl border border-white/10 text-slate-200 text-[10px] font-bold px-3 py-1.5 rounded-lg opacity-0 group-hover:opacity-100 transition-all duration-300 whitespace-nowrap pointer-events-none shadow-xl translate-x-2 group-hover:translate-x-0">
                    Mis Apuntes
                </span>
            </button>
        </div>
    );
};

export default FloatingTools;
