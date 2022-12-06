import { useEffect } from "react";

function Splash () {

  useEffect(() => {
    document.title = "Cyberspace Film Repository";
  }, []);

  return (
    <div className="splash-page">
      <h1>Welcome to the Cyberspace Film Repository</h1>
    </div>
  )
};

export default Splash;