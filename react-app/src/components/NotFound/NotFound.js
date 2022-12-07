 import { useEffect } from 'react';
import { Link } from 'react-router-dom';

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
        <Link to="/">Return Home</Link>
      </p>
    </div>
  </div>
  )
}


export default NotFound;