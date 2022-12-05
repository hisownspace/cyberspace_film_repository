import { Modal } from '../../context/Modal';
import DeleteFilm from "./DeleteFilm";
import "./DeleteFilm.css";

function DeleteFilmModal({ showModal, setShowModal, title, id }) {

  return (
    <>
      {showModal && (
        <Modal  onClose={() => setShowModal(false)}>
          <DeleteFilm title={title} id={id} setShowModal={setShowModal} />
        </Modal>
      )}
    </>
  );
}

export default DeleteFilmModal;