import axios from "axios";

const API_URL = "http://127.0.0.1:5000";

export const sendMessage = async (message, user_id) => {
  const res = await axios.post(`${API_URL}/chat/`, { message, user_id });
  return res.data;
};

export const getHistory = async (user_id) => {
  const res = await axios.get(`${API_URL}/history/${user_id}`);
  return res.data;
};
