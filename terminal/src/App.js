import { ReactTerminal } from "react-terminal";
import "./App.css";

function App(props) {
  // Define commands here
  const commands = {
    play: "The story takes place in a utopia Ihleda with a dark secret:- The balance of the utopia’s happiness Is caused by entrapping the Saint Maglena within a secret location of the headquarters. The story centresw around 17 yr old Anubis, who is tasked with setting Amglena free after he receivers message from the saint within a dream.",
  };

  // return <ReactTerminal commands={commands} />;
  return (
    <div className="terminal" style={{ maxHeight: "20px" }}>
      <ReactTerminal
        commands={commands}
        // themes={{
        //   themeBGColor: "#272B36",
        //   themeToolbarColor: "#DBDBDB",
        //   themeColor: "#FFFEFC",
        //   themePromptColor: "#a917a8",
        // }}
        theme="dark"
      />
    </div>
  );
}

export default App;
