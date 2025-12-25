export default function ChatMessage({ role, text, sources }) {
  return (
    <div className={`message ${role}`}>
      {text}

      {sources && (
        <div className="sources">
          Sources: {sources.join(", ")}
        </div>
      )}
    </div>
  );
}
