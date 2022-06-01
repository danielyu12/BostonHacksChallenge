import React from 'react';
import axios from 'axios';
import '../Task/Task.css';

const task = (props) => {
  const handleRemove = () => {
    axios
      .post('http://localhost:5000/update', {
        type: 'delete',
        message: props.task,
      })
      .then((res) => {
        console.log(res);
      })
      .catch((err) => {
        console.log(err);
      });
    window.location.reload();
  };
  return (
    <div className="individual-task">
      <p>{props.task}</p>
      <button onClick={handleRemove}>Remove</button>
    </div>
  );
};

export default task;
