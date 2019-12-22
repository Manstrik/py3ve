class Hello extends React.Component {
    render() {
        return <div>Привет, {this.props.toWhat}</div>;
    }
}

function cry() {
    console.log('Тсссс');
    ReactDOM.render(
        <Hello toWhat='Влад'/>,
        document.getElementById('reactplace')
    );
} // https://babeljs.io/docs/en/configuration