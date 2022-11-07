import Terminal from "./components/terminal";
//import frame from "./monitor.png";

function App() {
  return (
    <>
      <div className="parent">
        {/*<img className="monitor" src={frame} alt="monitor-frames" />*/}
        {/*<img className="frame"
          src="https://www.pngkey.com/png/detail/71-719419_old-tv-frame-png-siteframes-co-display-device.png"
          alt="Old Tv Frame Png Siteframes Co - Display Device@pngkey.com"
        ></img>*/}
        <Terminal className="term" />
      </div>
    </>
  );
}

export default App;
