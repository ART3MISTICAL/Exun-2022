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
          "The story takes place in a utopia Ihleda with a dark secret and centres around 17 yr old Anubis, who is tasked with setting Maglena free after he receivers a message from the saint within a dream.",
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
        return [
          "Once in the library, you finally find an ancient scripture that shows that Armageddon is a basement beneath the headquarters of the utopia, where Maglena was trappedby his trival Yacub.",
          <br />,
          <br />,
          "The script gives you two maps. Choose one:",
          <br />,
          <br />,
          "Game over, Type 'play' to play again",
          <br />,
          <br />,
          "a) One through the forest",
          <br />,
          "b) One through the city market",
        ];
      },
      b: () => {
        setIndex((prevState) => "start");
        return [
          "The father refused to tell Anubis the location and grounded him…",
          <br />,
          <br />,
          'Game over, Type "play" to play again',
        ];
      },
    },
    1.1: {
      a: () => {
        setIndex((prevState) => "start");
        return [
          "You enter through the forest and see a huge cherry blossom tree. Rather unusual.",
          <br />,
          <br />,
          "Break a branch of the tree.",
          <br />,
          <br />,
          "Transported to Armageddon gates.",
          <br />,
          <br />,
          "You open the gates, and in come a flurry of zombies.",
          <br />,
          <br />,
          "You die because you chose to travel from the forest and didnt have a weapon",
          <br />,
          <br />,
          "Game over, Type 'play' to play again",
        ];
      },
      b: () => {
        setIndex((prevState) => "1.2");
        return [
          "While travelling through the markets, you find a sword and a bow and arrow in the streets.",
          <br />,
          <br />,
          "Untouched. Ignored.",
          <br />,
          "Pick branch.",
          <br />,
          "Transported to Armageddon Gates.",
          <br />,
          <br />,
          "You open the gates, and in come a flurry of zombies.",
          <br />,
          <br />,
          "a) Use sword to fight the zombies.",
          <br />,
          "b) Use bow and arrow to fight the zombies.",
          <br />,
          "c) Try to run away.",
        ];
      },
    },
    1.2: {
      a: () => {
        setIndex((prevState) => "1.3");
        return [
          "You defeat the zombies.",
          <br />,
          <br />,
          "After defeating, you set to free Maglena… but he warns you that Yacub is behind you.",
          <br />,
          <br />,
          "You turn out to find the great nemesis, the evil yacub.",
          <br />,
          //<br />,
          "He is rather… familiar.",
          <br />,
          //<br />,
          "Almost too familiar.",
          <br />,
          <br />,
          "Thus the great nemesis of Maglena was, infact, your father.",
          <br />,
          <br />,
          "a) Use Sword to defeat Yacub and help Maglena",
          <br />,
          //<br />,
          "b) Help Yacub Kill Maglena",
        ];
      },
      b: () => {
        setIndex((prevState) => "1.3");
        return [
          "You defeat the zombies.",
          <br />,
          <br />,
          "After defeating, you set to free Maglena… but he warns you that Yacub is behind you.",
          <br />,
          <br />,
          "You turn out to find the great nemesis, the evil yacub.",
          <br />,
          //<br />,
          "He is rather… familiar.",
          <br />,
          //<br />,
          "Almost too familiar.",
          <br />,
          <br />,
          "Thus the great nemesis of Maglena was, infact, your father.",
          <br />,
          <br />,
          "a) Use Sword to defeat Yacub and help Maglena",
          <br />,
          //<br />,
          "b) Help Yacub Kill Maglena",
        ];
      },
      c: () => {
        setIndex((prevState) => "start");
        return [
          "Zombies kill you",
          <br />,
          <br />,
          'Game over, Type "play" to play again',
        ];
      },
    },
    1.3: {
      a: () => {
        setIndex((prevState) => "start");
        return [
          "Defeating your father, his title now belongs to you",
          <br />,
          <br />,
          "But Maglena, the ever-forgiving and kind wizard, thanks you for your service and instead of being afraid.",
          <br />,
          <br />,
          "Brave Ending",
          <br />,
          <br />,
          `Type "play" to play again`,
        ];
      },
      b: () => {
        setIndex((prevState) => "start");
        return [
          "With Maglena gone and nothing to sustain Ihleda, The utopia once again went back to what it was before 2025… A desolate land. Eventually overtaking your father’s position as the great evil wizard, you are shunned away from Ihleda by its citizens as they struggle to rebuild their lives after losing everything.",
          <br />,
          <br />,
          "Evil Ending",
          <br />,
          <br />,
          `Type "play" to play again`,
        ];
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
