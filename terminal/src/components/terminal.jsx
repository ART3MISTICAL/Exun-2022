import { ReactTerminal } from "react-terminal";
import '../terminal.module.css'


function App(props) {
	const commands = {
		play: "The story takes place in a utopia Ihleda with a dark secret:- The balance of the utopia's happiness Is caused by entrapping the Saint Maglena within a secret location of the headquarters. The story centresw around 17 yr old Anubis, who is tasked with setting Amglena free after he receivers a message from the saint within a dream.",
	};
	return (
		<div className="terminal-space">
			<ReactTerminal className="terminal"
				commands={commands}
				theme = "material-dark"
				showControlBar = {false}
				prompt = '>'
				welcomeMessage = 'Type "play" to play'
			/>
		</div>
	);
}

export default App;