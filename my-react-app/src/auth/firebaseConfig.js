// firebase.js
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { GoogleAuthProvider, getAuth } from "firebase/auth";

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyAveg-0fwFC8AbFvlIZSKbJpixIQzYMy5o",
  authDomain: "researchai-2d02e.firebaseapp.com",
  projectId: "researchai-2d02e",
  storageBucket: "researchai-2d02e.appspot.com",
  messagingSenderId: "760074984241",
  appId: "1:760074984241:web:359f722550b6c43fb86e10",
  measurementId: "G-987EBRNBXM"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
const provider = new GoogleAuthProvider();
const auth = getAuth(app);

export { app, analytics, provider, auth };
