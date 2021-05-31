class Intro extends React.Component {
  render() {
    return (
      <div class="">
        <h1>Cryptofarm - Become a digital farmer!</h1>
        <p id="cow">&#128004;</p>
        <a href="login_view">Login to start farming</a>
      </div>
    );
  }
}

ReactDOM.render(<Intro />, document.querySelector("#intro"));
