import { ReactTerminal } from "react-terminal";
import "../terminal.module.css";
import React, { useState } from "react";

function App(props) {
  const [index, setIndex] = useState("start");
  //const commands = {
  //  play: "The story takes place in a utopia Ihleda with a dark secret:- The balance of the utopia's happiness Is caused by entrapping the Saint Maglena within a secret location of the headquarters. The story centresw around 17 yr old Anubis, who is tasked with setting Amglena free after he receivers a message from the saint within a dream.",

  //};

  const array = {
    start: {
      play: () => {
        setIndex((prevState) => "1");
        return [
          "The story takes place in a utopia Ihleda with a dark secret and centres around 17 yr old Anubis, who is tasked with setting Amglena free after he receivers a message from the saint within a dream.",
          <br />,
          <br />,
          "Anubis wakes up from a dream and recounts the prophecy he received in his dream: ",
          // <br />,
          <br />,
          "He is meant to find Maglena and set him free from a place named Armageddon that he doesn't know the location of.",
          <br />,
          <br />,
          "He is offered two choices:",
          <br />,
          <br />,
          "a)Look for Armageddon in the Ihleda national library maps",
          <br />,
          <br />,
          "b) Ask his father (the president of Ilheda) about Armageddon",
        ];
      },
    },
    1: {
      a: () => {
        setIndex((prevState) => "1.1");
        return "a option";
      },
      b: () => {
        setIndex((prevState) => prevState + 2);
        return "b option";
      },
    },
    1.1: {
      a: () => {
        setIndex((prevState) => prevState + 1);
        return "a situation";
      },
      b: () => {
        setIndex((prevState) => prevState + 2);
        return "a sit";
      },
    },
  };

  return (
    <div className="terminal-space">
      <ReactTerminal
        className="terminal"
        commands={array[index]}
        theme="material-dark"
        showControlBar={false}
        prompt=">"
        welcomeMessage='Type "play" to play '
      />
    </div>
  );
}

export default App;
