import { Modal } from '../../context/Modal';
import DeleteActor from './DeleteActor';
import "./DeleteActor.css";

function DeleteActorModal({ showModal, setShowModal, name, id }) {

  return (
    <>
      {showModal && (
        <Modal  onClose={() => setShowModal(false)}>
          <DeleteActor name={name} id={id} setShowModal={setShowModal} />
        </Modal>
      )}
    </>
  );
}

export default DeleteActorModal;