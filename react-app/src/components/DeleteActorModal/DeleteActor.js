import { useHistory } from "react-router-dom";
import { useEffect } from "react";

function DeleteActor({ name, id, setShowModal }) {
  const history = useHistory();

  const handleDelete = async () => {
    const res = await fetch(`/api/actors/${id}`, {
      method: "DELETE",
    })
    if (res.ok) {
      history.push("/");
    } else {
      console.log(await res.json().message);
    }
  };

  return (
    <div className="modal-box">
      <div className="modal" >
        <p>
          Are you sure you want to delete the entry for {name}?
        </p>
      </div>
      <div className="modal-buttons">
        <button className="delete-confirm" onClick={handleDelete}>Yes</button>
        <button className="delete-confirm" onClick={() => setShowModal(false)}>No</button>
      </div>
    </div>
  )
};

export default DeleteActor;