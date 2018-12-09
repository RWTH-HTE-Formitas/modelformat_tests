import React, { Component } from 'react';
import Scene from "./Scene";

const styles = {
    width: "100vw",
    height: "100vh"
};

class Visualizer extends Component {

    modelLocation = "https://raw.githubusercontent.com/mrdoob/three.js/dev/examples/models/obj/tree.obj";

    render() {
        return (
            <div style={styles}>
                <Scene modelLocation={this.modelLocation} />
                <div style={{ zIndex: 1, position: "absolute" }}></div>
            </div>
        );
    }
}

export default Visualizer;
