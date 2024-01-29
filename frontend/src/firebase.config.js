import { getApp, getApps, initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore";
import { getStorage } from "firebase/storage";

const firebaseConfig = {
  apiKey: "AIzaSyDAqgUTEBsI_Ow56Ldl-HRuV9Us1PXVLXk",
  authDomain: "fitness-1a740.firebaseapp.com",
  projectId: "fitness-1a740",
  storageBucket: "fitness-1a740.appspot.com",
  messagingSenderId: "845212874715",
  appId: "1:845212874715:web:acebdf585a0f05751559fe",
  measurementId: "G-WXL7FNM7KP",
};

const app = getApps.length > 0 ? getApp() : initializeApp(firebaseConfig);

const firestore = getFirestore(app);
const storage = getStorage(app);

export { app, firestore, storage };
