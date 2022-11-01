import { useState, useEffect } from "react";

function AddActor() {
  const [name, setName] = useState("");
  const [dateOfBirth, setDateOfBirth] = useState("");
  const [placeOfBirth, setPlaceOfBirth] = useState("");
  const [photo, setPhoto] = useState("");

  const handleSubmit = async e =>{
    e.preventDefault()

    const actorForm = {
      name,
      "date_of_birth": dateOfBirth,
      "place_of_birth": placeOfBirth,
      photo
    }

    const res = await fetch("/api/actors",
    {
      method: "POST",
      headers: { "Content-Type": "application/json"
      },
      body: JSON.stringify(actorForm)
    });

    if (res.ok) {
      const actor = await res.json();
      console.log(actor);
    } else {
      console.log(res.status)
      const data = await res.json();
      if (data.errors) {
        console.log(data.errors)
      }
    }
  }
  
  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="name">
        Name: 
      </label>
      <input
        id="name"
        value={name}
        onChange={e => setName(e.target.value)}
      />
      <label htmlFor="dateOfBirth">
        Date of Birth: 
      </label>
      <input
        id="dateOfBirth"
        value={dateOfBirth}
        onChange={e => setDateOfBirth(e.target.value)}
        />
      <label htmlFor="placeOfBirth">
        Place of Birth: 
      </label>
      <input
        id="placeOfBirth"
        value={placeOfBirth}
        onChange={e => setPlaceOfBirth(e.target.value)}
        />
      <label htmlFor="photo">
        Photo Url: 
      </label>
      <input
        id="photo"
        value={photo}
        onChange={e => setPhoto(e.target.value)}
        />
      <button>Submit</button>
    </form>
  )
}

export default AddActor;