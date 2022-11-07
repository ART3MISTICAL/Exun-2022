import Terminal from "./components/terminal";
//import frame from "./monitor.png";

function App() {
  return (
    <>
      <div className="ct">
				Press F11 for fullscreen
			</div>
      <div className="parent">
        <Terminal className="term" />
      </div>
    </>
  );
}

export default App;
