import { ReactTerminal } from "react-terminal";
import './terminal.module.css'


function App(props) {
	const commands = {
		play: "jackharper",
	};
	return (
		<div className="terminal-space">
			<ReactTerminal className="terminal"
				commands={commands}
				theme="dark"
			/>
		</div>
	);
}

export default App;
