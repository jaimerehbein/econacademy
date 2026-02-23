import { useState, useEffect } from 'react';

export const useContent = (subjectId) => {
    const [content, setContent] = useState('');
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        if (!subjectId) return;

        const fetchContent = async () => {
            setLoading(true);
            setError(null);
            try {
                // Find filename based on ID if we had a map, for now we assume subjectId is the filename part
                // Actually we can pass the specific path.
                const response = await fetch(`/program/${subjectId}.md`);
                if (!response.ok) throw new Error('Contenido no encontrado');
                const text = await response.text();
                setContent(text);
            } catch (err) {
                setError(err.message);
            } finally {
                setLoading(false);
            }
        };

        fetchContent();
    }, [subjectId]);

    return { content, loading, error };
};
