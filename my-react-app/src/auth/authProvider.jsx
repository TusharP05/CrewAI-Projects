// AuthProvider.js
import React, { useEffect, useState } from "react";
import { signInWithRedirect , getRedirectResult} from "firebase/auth";
import{auth, provider} from "./firebaseConfig"

const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);

  useEffect(() => {
    const authenticateUser = async () => {
      try {
        const result = await getRedirectResult(auth);
        if (result) {
          // User signed in
          setUser(result.user);
        } else {
          // No user signed in, initiate the redirect
          signInWithRedirect(auth, provider);
        }
      } catch (error) {
        console.error("Authentication error:", error);
      }
    };

    authenticateUser();
  }, []);

  if (!user) {
    return <div>Loading...</div>; // Show a loading indicator while waiting for sign-in
  }

  return <>{children}</>;
};

export default AuthProvider;
