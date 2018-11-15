import React, { Component } from 'react';
import Scene from "./Scene";

const styles = {
    width: "100vw",
    height: "100vh"
};

class Visualizer extends Component {

    modelLocation = "data/dae2gltf/model1.gltf";

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
