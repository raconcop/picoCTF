import java.io.*;
import java.util.*;  
public class SafeOpener {





    // Main method
    public static void main(String args[]) throws IOException {

        // Gets the keyboard inputs as a buffered read
        BufferedReader keyboard = new BufferedReader(new InputStreamReader(System.in));
        Base64.Encoder encoder = Base64.getEncoder();
        String encodedkey = "";
        String key = "";
        int i = 0;
        boolean isOpen;
        

        while (i < 3) {


            // Asks for password input
            System.out.print("Enter password for the safe: ");
            key = keyboard.readLine();


            // Encoded version of what we input
            encodedkey = encoder.encodeToString(key.getBytes());
            System.out.println(encodedkey);
              

            // True or false if what we entered is correct or not
            isOpen = openSafe(encodedkey);
            if (!isOpen) {
                System.out.println("You have  " + (2 - i) + " attempt(s) left");
                i++;
                continue;
            }
            break;
        }
    }
    
    public static boolean openSafe(String password) {

        // What we input has to match this here
        String encodedkey = "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz";
        
        if (password.equals(encodedkey)) {
            System.out.println("Sesame open");
            return true;
        }
        else {
            System.out.println("Password is incorrect\n");
            return false;
        }
    }
}