import React, { useState, useMemo } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, ReferenceLine } from 'recharts';

const Simulator = ({ configStr }) => {
    let config;
    try {
        config = JSON.parse(configStr);
    } catch (e) {
        return <div className="text-red-400 p-4 bg-red-500/10 backdrop-blur-md rounded-xl border border-red-500/20">Error parsing simulator config</div>;
    }

    const { component_type, variables, formula_js, pedagogical_insight } = config;

    // Initialize state with default values
    const [state, setState] = useState(() => {
        const initialState = {};
        variables.forEach(v => {
            initialState[v.name] = v.default;
        });
        return initialState;
    });

    const handleSliderChange = (name, value) => {
        setState(prev => ({ ...prev, [name]: parseFloat(value) }));
    };

    // Generate data based on formula
    const chartData = useMemo(() => {
        if (component_type !== 'graph_2d') return [];

        const data = [];
        try {
            const context = { ...state, Math };
            const keys = Object.keys(context);
            const values = Object.values(context);
            const fn = new Function(...keys, 'x', `return ${formula_js}`);

            for (let i = -50; i <= 50; i += 1) {
                const x = i / 5; // -10 to 10
                let y = 0;
                try {
                    y = fn(...values, x);
                } catch (err) {
                    console.error("Formula error", err);
                }
                data.push({ x, y });
            }
        } catch (e) {
            console.error("Error generating data", e);
        }
        return data;
    }, [state, formula_js, component_type]);

    // Calculate balance sheet derived value
    const balanceDerived = useMemo(() => {
        if (component_type !== 'balance_sheet') return 0;
        try {
            const context = { ...state, Math };
            const keys = Object.keys(context);
            const values = Object.values(context);
            const fn = new Function(...keys, `return ${formula_js}`);
            return fn(...values);
        } catch (e) {
            return 0;
        }
    }, [state, formula_js, component_type]);

    return (
        <div className="glass-panel rounded-3xl p-8 shadow-[0_0_50px_rgba(79,70,229,0.1)] my-12 text-white relative overflow-hidden group">
            <div className="absolute top-0 left-0 w-full h-[2px] bg-gradient-to-r from-cyan-400 via-indigo-500 to-purple-500 shadow-[0_0_10px_rgba(99,102,241,0.5)]"></div>

            {/* Ambient Background Glow for Simulator */}
            <div className="absolute -top-32 -right-32 w-64 h-64 bg-indigo-500/10 rounded-full blur-[80px] group-hover:bg-indigo-500/20 transition-colors duration-700 pointer-events-none"></div>

            <h3 className="text-2xl md:text-3xl font-bold mb-8 flex items-center gap-4 text-transparent bg-clip-text bg-gradient-to-r from-white to-slate-400">
                <span className="bg-white/5 text-indigo-400 p-2.5 rounded-xl border border-white/10 shadow-lg backdrop-blur-md">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M3 3v18h18" /><path d="m19 9-5 5-4-4-3 3" /></svg>
                </span>
                Simulador Interactivo
            </h3>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-8 relative z-10">
                <div className="md:col-span-1 space-y-6 bg-white/5 backdrop-blur-md p-6 rounded-2xl border border-white/5 shadow-inner">
                    <h4 className="text-[11px] font-bold uppercase tracking-widest text-indigo-400/80 mb-6 flex items-center gap-2">
                        <span className="w-1.5 h-1.5 rounded-full bg-indigo-400 animate-pulse"></span>
                        Panel de Control
                    </h4>
                    {variables.map(v => (
                        <div key={v.name} className="space-y-3">
                            <div className="flex justify-between text-sm items-center">
                                <label className="font-medium text-slate-300">{v.label || v.name}</label>
                                <span className="text-cyan-400 font-mono font-bold bg-cyan-900/30 border border-cyan-500/20 px-2 py-0.5 rounded shadow-[0_0_10px_rgba(6,182,212,0.1)]">{state[v.name]}</span>
                            </div>
                            <input
                                type="range"
                                min={v.min}
                                max={v.max}
                                step={v.step || 1}
                                value={state[v.name]}
                                onChange={(e) => handleSliderChange(v.name, e.target.value)}
                                className="w-full h-1.5 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-cyan-400 hover:accent-cyan-300 transition-all focus:outline-none focus:ring-2 focus:ring-cyan-500/50"
                            />
                        </div>
                    ))}

                    <div className="mt-8 pt-6 border-t border-white/5">
                        <div className="text-sm bg-indigo-500/10 backdrop-blur-md text-slate-300 p-4 rounded-xl border border-indigo-500/20 leading-relaxed italic relative overflow-hidden">
                            <div className="absolute left-0 top-0 bottom-0 w-1 bg-indigo-500 shadow-[0_0_10px_rgba(99,102,241,0.5)]"></div>
                            {pedagogical_insight}
                        </div>
                    </div>
                </div>

                <div className="md:col-span-2 bg-slate-900/50 rounded-2xl p-4 border border-white/5 flex items-center justify-center min-h-[350px] shadow-inner backdrop-blur-sm relative">
                    {component_type === 'graph_2d' && (
                        <div className="w-full h-full min-h-[350px] relative z-10">
                            <ResponsiveContainer width="100%" height="100%">
                                <LineChart data={chartData} margin={{ top: 20, right: 30, left: 20, bottom: 20 }}>
                                    <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" vertical={false} />
                                    <XAxis dataKey="x" stroke="#64748b" tick={{ fill: '#64748b', fontSize: 12 }} axisLine={{ stroke: '#334155' }} />
                                    <YAxis stroke="#64748b" tick={{ fill: '#64748b', fontSize: 12 }} axisLine={{ stroke: '#334155' }} />
                                    <Tooltip
                                        contentStyle={{ backgroundColor: 'rgba(15, 23, 42, 0.9)', backdropFilter: 'blur(8px)', borderColor: 'rgba(255,255,255,0.1)', color: '#f8fafc', borderRadius: '12px', boxShadow: '0 10px 25px -5px rgba(0, 0, 0, 0.5)' }}
                                        itemStyle={{ color: '#22d3ee', fontWeight: 'bold' }}
                                    />
                                    <ReferenceLine x={0} stroke="#475569" strokeDasharray="3 3" />
                                    <ReferenceLine y={0} stroke="#475569" strokeDasharray="3 3" />
                                    <Line type="monotone" dataKey="y" stroke="#22d3ee" strokeWidth={3} dot={false} activeDot={{ r: 8, fill: '#22d3ee', stroke: '#fff', strokeWidth: 2 }} />
                                </LineChart>
                            </ResponsiveContainer>
                        </div>
                    )}

                    {component_type === 'balance_sheet' && (
                        <div className="w-full h-full flex flex-col items-center justify-center space-y-10 p-6 relative z-10">
                            <h4 className="text-xl md:text-2xl font-bold tracking-tight text-transparent bg-clip-text bg-gradient-to-r from-emerald-400 to-cyan-400">Balance General Interactivo</h4>

                            <div className="flex w-full max-w-2xl items-end justify-center gap-6 md:gap-12 h-56">
                                {/* Activo */}
                                <div className="w-1/3 flex flex-col justify-end items-center h-full relative group">
                                    <span className="absolute -top-10 font-mono font-extrabold text-emerald-400 text-xl tracking-tight drop-shadow-[0_0_8px_rgba(52,211,153,0.5)]">${state.activo || 0}</span>
                                    <div
                                        className="w-full bg-gradient-to-t from-emerald-900/80 to-emerald-500/80 rounded-t-xl transition-all duration-500 shadow-[0_0_20px_rgba(16,185,129,0.2)] group-hover:shadow-[0_0_30px_rgba(16,185,129,0.4)] border border-emerald-400/30 backdrop-blur-sm"
                                        style={{ height: '100%' }}
                                    ></div>
                                    <span className="mt-5 font-bold tracking-[0.2em] text-emerald-200/80 text-xs">ACTIVO</span>
                                </div>

                                <span className="text-slate-500/50 font-light mb-10 text-4xl">=</span>

                                {/* Pasivo + Patrimonio */}
                                <div className="w-1/3 flex flex-col justify-end items-center h-full">
                                    <div className="w-full flex justify-between px-2 absolute -top-10 font-mono font-extrabold text-base md:text-lg">
                                        <span className="text-rose-400 drop-shadow-[0_0_8px_rgba(244,63,94,0.5)]">${state.pasivo || 0}</span>
                                        <span className="text-sky-400 drop-shadow-[0_0_8px_rgba(56,189,248,0.5)]">${Math.max(0, balanceDerived)}</span>
                                    </div>

                                    <div className="w-full h-full flex flex-col justify-end gap-1.5">
                                        {/* Patrimonio (Calculated) */}
                                        <div
                                            className="w-full bg-gradient-to-t from-sky-900/80 to-sky-500/80 rounded-t-xl transition-all duration-500 shadow-[0_0_20px_rgba(14,165,233,0.2)] border border-sky-400/30 flex items-center justify-center backdrop-blur-sm relative overflow-hidden group"
                                            style={{ height: `${Math.max(0, (balanceDerived / (state.activo || 1)) * 100)}%` }}
                                        >
                                            <div className="absolute inset-0 bg-gradient-to-t from-transparent to-white/10"></div>
                                            {balanceDerived > 0 && <span className="text-[10px] font-bold text-sky-100 rotate-90 md:rotate-0 tracking-widest z-10">CAPITAL</span>}
                                        </div>

                                        {/* Pasivo */}
                                        <div
                                            className="w-full bg-gradient-to-t from-rose-900/80 to-rose-500/80 rounded-b-md transition-all duration-500 shadow-[0_0_20px_rgba(244,63,94,0.2)] border border-rose-400/30 flex items-center justify-center backdrop-blur-sm relative overflow-hidden group"
                                            style={{ height: `${Math.max(0, ((state.pasivo || 0) / (state.activo || 1)) * 100)}%` }}
                                        >
                                            <div className="absolute inset-0 bg-gradient-to-b from-transparent to-black/20"></div>
                                            {(state.pasivo || 0) > 0 && <span className="text-[10px] font-bold text-rose-100 rotate-90 md:rotate-0 tracking-widest z-10">PASIVO</span>}
                                        </div>
                                    </div>
                                    <span className="mt-5 font-bold tracking-[0.2em] text-slate-400 text-[10px] md:text-xs flex flex-col items-center leading-tight">
                                        <span>PASIVO+</span>
                                        <span>CAPITAL</span>
                                    </span>
                                </div>
                            </div>

                            <div className="bg-white/5 backdrop-blur-md px-6 py-2.5 rounded-full border border-white/10 mt-6 md:mt-10 text-xs md:text-sm font-mono text-slate-300 shadow-xl">
                                Ecuación Balanceada: <span className="text-emerald-400 font-bold">${state.activo || 0}</span> = <span className="text-rose-400 font-bold">${state.pasivo || 0}</span> + <span className="text-sky-400 font-bold">${Math.max(0, balanceDerived)}</span>
                            </div>
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
};

export default Simulator;
