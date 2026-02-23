import React, { useState } from 'react';
import Sidebar from './Sidebar';
import FloatingTools from './FloatingTools';
import NotesPanel from './NotesPanel';
import { Flame, BookOpen, Menu } from 'lucide-react';

const Layout = ({ children }) => {
    const [isNotesOpen, setIsNotesOpen] = useState(false);
    const [isSidebarOpen, setIsSidebarOpen] = useState(false);

    return (
        <div className="flex bg-study-bg min-h-screen text-study-text selection:bg-indigo-500/30 selection:text-white transition-colors duration-500">
            <Sidebar isOpen={isSidebarOpen} setIsOpen={setIsSidebarOpen} />

            {/* Overlay for mobile sidebar */}
            {isSidebarOpen && (
                <div
                    className="fixed inset-0 bg-black/60 backdrop-blur-sm z-40 lg:hidden"
                    onClick={() => setIsSidebarOpen(false)}
                />
            )}

            <main className="flex-1 lg:ml-80 min-h-screen relative overflow-x-hidden flex flex-col w-full">
                {/* Personal Progress Dashboard (Discrete Top Bar) - Glassmorphism */}
                <header className="w-full bg-slate-900/60 backdrop-blur-2xl border-b border-white/10 px-4 md:px-8 py-4 sticky top-0 z-30 flex items-center justify-between shadow-xl shadow-black/20">
                    <div className="flex items-center gap-3">
                        <button
                            onClick={() => setIsSidebarOpen(true)}
                            className="lg:hidden p-2 -ml-2 text-slate-300 hover:text-white hover:bg-white/10 rounded-lg transition-colors"
                        >
                            <Menu size={20} />
                        </button>
                        <span className="font-semibold text-slate-200 tracking-wide text-xs md:text-sm hidden sm:inline-block">Hola, Estudiante</span>
                        <span className="text-slate-600 hidden sm:inline-block">•</span>
                        <div className="flex items-center gap-1.5 text-orange-400 bg-orange-500/10 border border-orange-500/20 px-2 md:px-3 py-1 rounded-full font-bold text-[10px] md:text-xs shadow-[0_0_10px_rgba(249,115,22,0.2)]">
                            <Flame size={14} fill="currentColor" className="animate-pulse" />
                            <span className="hidden sm:inline-block">12 días de racha</span>
                            <span className="sm:hidden">12 días</span>
                        </div>
                    </div>
                    <div className="flex items-center gap-2 text-indigo-300 text-[10px] md:text-xs font-medium bg-indigo-500/10 px-2 md:px-3 py-1.5 rounded-lg border border-indigo-500/20 max-w-[50%] sm:max-w-none truncate shrink-0">
                        <BookOpen size={14} className="text-indigo-400 shrink-0" />
                        <span className="tracking-wide truncate">A40 Finanzas Corporativas</span>
                    </div>
                </header>

                <div className="max-w-4xl mx-auto px-4 sm:px-8 md:px-12 py-8 md:py-16 w-full relative z-10">
                    {children}
                </div>

                {/* Global floating study tools */}
                <FloatingTools onOpenNotes={() => setIsNotesOpen(true)} />
            </main>

            {/* Slide-out Personal Notes Editor */}
            <NotesPanel isOpen={isNotesOpen} onClose={() => setIsNotesOpen(false)} />
        </div>
    );
};

export default Layout;
