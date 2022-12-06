 import {useEffect } from 'react';


function NotFound () {

  useEffect(() => {
    document.title = "404: Not Found";
  }, []);

  return (
  <div className="not-found-main">
    <div className="not-found-box">
      <p className="not-found-message">
        404: Not Found
      </p>
      <p>
        <a href="/">Return Home</a>
      </p>
    </div>
  </div>
  )
}


export default NotFound;