import React, { useEffect, useState, memo } from 'react';
import { TrendingUp, BarChart2, Cpu, BookOpen, Globe, Activity } from 'lucide-react';

const iconComponents = {
    macro: { component: TrendingUp, color: '#f59e0b' }, // amber-500
    micro: { component: BarChart2, color: '#fb923c' }, // orange-400
    finanzas: { component: Cpu, color: '#f97316' }, // orange-500
    politica: { component: BookOpen, color: '#fbbf24' }, // amber-400
    internacional: { component: Globe, color: '#ea580c' }, // orange-600
    matematicas: { component: Activity, color: '#fcd34d' }, // amber-300
};

const SkillIcon = memo(({ type }) => {
    const IconComponent = iconComponents[type]?.component;
    return IconComponent ? <IconComponent size={20} color={iconComponents[type].color} /> : null;
});
SkillIcon.displayName = 'SkillIcon';

const skillsConfig = [
    // Inner Orbit
    { id: 'micro', orbitRadius: 110, size: 44, speed: 0.8, iconType: 'micro', phaseShift: 0, glowColor: 'amber', label: 'Microeconomía' },
    { id: 'politica', orbitRadius: 110, size: 44, speed: 0.8, iconType: 'politica', phaseShift: (2 * Math.PI) / 3, glowColor: 'amber', label: 'Economía Política' },
    { id: 'matematicas', orbitRadius: 110, size: 44, speed: 0.8, iconType: 'matematicas', phaseShift: (4 * Math.PI) / 3, glowColor: 'amber', label: 'Matemáticas Económicas' },
    // Outer Orbit
    { id: 'macro', orbitRadius: 200, size: 52, speed: -0.5, iconType: 'macro', phaseShift: 0, glowColor: 'orange', label: 'Macroeconomía' },
    { id: 'finanzas', orbitRadius: 200, size: 52, speed: -0.5, iconType: 'finanzas', phaseShift: (2 * Math.PI) / 3, glowColor: 'orange', label: 'Ingeniería Financiera' },
    { id: 'internacional', orbitRadius: 200, size: 52, speed: -0.5, iconType: 'internacional', phaseShift: (4 * Math.PI) / 3, glowColor: 'orange', label: 'Economía Internacional' },
];

const OrbitingSkill = memo(({ config, angle }) => {
    const [isHovered, setIsHovered] = useState(false);
    const { orbitRadius, size, iconType, label } = config;

    const x = Math.cos(angle) * orbitRadius;
    const y = Math.sin(angle) * orbitRadius;

    return (
        <div
            className="absolute top-1/2 left-1/2 transition-all duration-300 ease-out"
            style={{
                width: `${size}px`,
                height: `${size}px`,
                transform: `translate(calc(${x}px - 50%), calc(${y}px - 50%))`,
                zIndex: isHovered ? 20 : 10,
            }}
            onMouseEnter={() => setIsHovered(true)}
            onMouseLeave={() => setIsHovered(false)}
        >
            <div
                className={`
          relative w-full h-full p-2 bg-slate-800/90 backdrop-blur-md border border-white/10
          rounded-full flex items-center justify-center
          transition-all duration-300 cursor-pointer
          ${isHovered ? 'scale-125 shadow-2xl' : 'shadow-lg hover:shadow-xl'}
        `}
                style={{
                    boxShadow: isHovered
                        ? `0 0 30px ${iconComponents[iconType]?.color}60, 0 0 60px ${iconComponents[iconType]?.color}30`
                        : undefined
                }}
            >
                <SkillIcon type={iconType} />
                {isHovered && (
                    <div className="absolute -bottom-8 left-1/2 -translate-x-1/2 px-2.5 py-1 bg-slate-900/95 backdrop-blur-md rounded border border-white/10 text-[10px] font-bold tracking-widest uppercase text-white whitespace-nowrap pointer-events-none">
                        {label}
                    </div>
                )}
            </div>
        </div>
    );
});
OrbitingSkill.displayName = 'OrbitingSkill';

const GlowingOrbitPath = memo(({ radius, glowColor = 'cyan', animationDelay = 0 }) => {
    const glowColors = {
        amber: { primary: 'rgba(245, 158, 11, 0.4)', secondary: 'rgba(245, 158, 11, 0.1)', border: 'rgba(245, 158, 11, 0.2)' },
        orange: { primary: 'rgba(249, 115, 22, 0.4)', secondary: 'rgba(249, 115, 22, 0.1)', border: 'rgba(249, 115, 22, 0.2)' },
    };

    const colors = glowColors[glowColor] || glowColors.cyan;

    return (
        <div
            className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 rounded-full pointer-events-none"
            style={{
                width: `${radius * 2}px`,
                height: `${radius * 2}px`,
                animationDelay: `${animationDelay}s`,
            }}
        >
            <div
                className="absolute inset-0 rounded-full animate-pulse"
                style={{
                    background: `radial-gradient(circle, transparent 30%, ${colors.secondary} 70%, transparent 100%)`,
                    boxShadow: `inset 0 0 40px ${colors.secondary}`,
                    animation: 'pulse 4s ease-in-out infinite',
                    animationDelay: `${animationDelay}s`,
                }}
            />
            <div
                className="absolute inset-0 rounded-full"
                style={{ border: `1px solid ${colors.border}` }}
            />
        </div>
    );
});
GlowingOrbitPath.displayName = 'GlowingOrbitPath';

export default function OrbitingMasters() {
    const [time, setTime] = useState(0);
    const [isPaused, setIsPaused] = useState(false);

    useEffect(() => {
        if (isPaused) return;

        let animationFrameId;
        let lastTime = performance.now();

        const animate = (currentTime) => {
            const deltaTime = (currentTime - lastTime) / 1000;
            lastTime = currentTime;
            setTime(prevTime => prevTime + deltaTime);
            animationFrameId = requestAnimationFrame(animate);
        };

        animationFrameId = requestAnimationFrame(animate);
        return () => cancelAnimationFrame(animationFrameId);
    }, [isPaused]);

    const orbitConfigs = [
        { radius: 110, glowColor: 'amber', delay: 0 },
        { radius: 200, glowColor: 'orange', delay: 1.5 }
    ];

    return (
        <div
            className="relative w-full max-w-[450px] aspect-square flex items-center justify-center shrink-0 mx-auto md:mx-0 scale-75 md:scale-100"
            onMouseEnter={() => setIsPaused(true)}
            onMouseLeave={() => setIsPaused(false)}
        >
            {/* Central Hub Logo - the core of EconAcademy */}
            <div className="w-24 h-24 bg-gradient-to-br from-slate-900 to-black rounded-full flex flex-col items-center justify-center z-10 relative shadow-2xl border border-white/10 group-hover:border-amber-500/30 transition-colors">
                <div className="absolute inset-0 rounded-full bg-amber-500/20 blur-xl animate-pulse"></div>
                <div className="absolute inset-0 rounded-full bg-orange-500/10 blur-2xl animate-pulse" style={{ animationDelay: '1s' }}></div>
                <div className="relative z-10 flex flex-col items-center">
                    <span className="text-white font-black text-xl tracking-tighter">ECON</span>
                    <span className="text-transparent bg-clip-text bg-gradient-to-r from-amber-400 to-orange-400 text-xs font-black tracking-widest mt-[-2px]">ACADEMY</span>
                </div>
            </div>

            {/* Orbit Paths */}
            {orbitConfigs.map((config) => (
                <GlowingOrbitPath
                    key={`path-${config.radius}`}
                    radius={config.radius}
                    glowColor={config.glowColor}
                    animationDelay={config.delay}
                />
            ))}

            {/* Orbiting Icons */}
            {skillsConfig.map((config) => {
                const angle = time * config.speed + (config.phaseShift || 0);
                return (
                    <OrbitingSkill
                        key={config.id}
                        config={config}
                        angle={angle}
                    />
                );
            })}
        </div>
    );
}
