import React, { useEffect, useRef } from 'react';
import renderMathInElement from 'katex/dist/contrib/auto-render';
import 'katex/dist/katex.min.css';
import Simulator from './Simulator';
import ReactMarkdown from 'react-markdown';
import rehypeRaw from 'rehype-raw';
import mermaid from 'mermaid';

mermaid.initialize({
  startOnLoad: false,
  theme: 'dark',
  securityLevel: 'loose',
  fontFamily: 'Inter, sans-serif'
});

const MarkdownRenderer = ({ content }) => {
  const containerRef = useRef(null);

  useEffect(() => {
    if (containerRef.current) {
      // Render Math
      renderMathInElement(containerRef.current, {
        delimiters: [
          { left: '$$', right: '$$', display: true },
          { left: '$', right: '$', display: false },
          { left: '\\(', right: '\\)', display: false },
          { left: '\\[', right: '\\]', display: true }
        ],
        throwOnError: false
      });

      // Render Mermaid
      setTimeout(() => {
        try {
          mermaid.init(undefined, '.mermaid');
        } catch (e) {
          console.error("Mermaid error:", e);
        }
      }, 100);
    }
  }, [content]);

  if (!content) return null;

  // If the file is pre-built HTML (starts with <div or <article),
  // inject it directly so tags are not shown as raw text.
  const trimmed = content.trimStart();
  if (trimmed.startsWith('<div') || trimmed.startsWith('<article')) {
    return (
      <div
        ref={containerRef}
        className="markdown-content"
        dangerouslySetInnerHTML={{ __html: content }}
      />
    );
  }

  return (
    <div ref={containerRef} className="markdown-content">
      <ReactMarkdown
        rehypePlugins={[rehypeRaw]}
        components={{
          div: ({ node, ...props }) => {
            if (props['data-component'] === 'simulator') {
              return <Simulator configStr={props['data-config']} />;
            }
            return <div {...props} />;
          }
        }}
      >
        {content}
      </ReactMarkdown>
    </div>
  );
};

export default MarkdownRenderer;
