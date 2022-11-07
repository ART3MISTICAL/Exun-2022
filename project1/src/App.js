import React, { Component } from "react";
import Terminal from "terminal-in-react";

class App extends Component {
  showMsg = () => "Hello World";

  render() {
    return (
      <div>
        <Terminal
          color="red"
          backgroundColor="black"
          barColor="black"
          style={{ fontWeight: "bold", fontSize: "1em" }}
          commands={{
            "open-google": () =>
              window.open("https://www.google.com/", "_blank"),
            showmsg: this.showMsg,
            popup: () => alert("Terminal in React"),
          }}
          descriptions={{
            "open-google": "opens google.com",
            showmsg: "shows a message",
            alert: "alert",
            popup: "alert",
          }}
          msg="You can write anything here. Example - Hello! My name is Foo and I like Bar."
        />
        {/* <Terminal
          commands={{
            "type-text": (args, print, runCommand) => {
              const text = args.slice(1).join("");
              // print("");
              for (let i = 0; i < text.length; i += 1) {
                setTimeout(() => {
                  runCommand(`edit-line ${text.slice(0, i + 1)}`);
                }, 100 * i);
              }
            },
          }} */}
      </div>
    );
  }
}

export default App;
