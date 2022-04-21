import React, { useEffect, useState } from 'react';
import Task from '../task/task.js';
import axios from 'axios';

const Tasks = (props) => {
  useEffect(() => {
    axios
      .get('http://localhost:5000/update')
      .then((res) => {
        setState({ taskList: res.data.todos });
      })
      .catch((err) => {
        console.log(err);
      });
  }, []);

  const [state, setState] = useState({
    taskList: [],
  });

  return (
    <div>
      {state.taskList.map((task) => (
        <Task task={task} />
      ))}
    </div>
  );
};

export default Tasks;
