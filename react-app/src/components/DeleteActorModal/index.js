import React, { useEffect, useState } from 'react';
import { Modal } from '../../context/Modal';
import DeleteActor from './DeleteActor';
import "./DeleteActor.css";

function DeleteActorModal({ showModal, setShowModal, name, id }) {

  return (
    <>
      {/* <button onClick={() => setShowModal(true)}>Log In</button> */}
      {showModal && (
        <Modal  onClose={() => setShowModal(false)}>
          <DeleteActor name={name} id={id} setShowModal={setShowModal} />
        </Modal>
      )}
    </>
  );
}

export default DeleteActorModal;