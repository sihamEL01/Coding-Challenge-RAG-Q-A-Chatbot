export default function Suggestions({ onSelect }) {
  const items = [
    "Who is the narrator of Treasure Island?",
    "Where does Jim Hawkins live?",
    "At which inn does the story begin?"
  ];

  return (
    <div className="suggestions">
      {items.map((q, i) => (
        <div
          key={i}
          className="suggestion"
          onClick={() => onSelect(q)}
        >
          {q}
        </div>
      ))}
    </div>
  );
}
