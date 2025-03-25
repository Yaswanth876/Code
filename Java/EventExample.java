import javax.swing.*;  
import java.awt.event.*;  

public class EventExample {  
    public static void main(String[] args) {  
        JFrame frame = new JFrame("Event-Driven Program");  // Creating a frame
        JButton button = new JButton("Click Me!");  // Creating a button  
        
        button.setBounds(100, 100, 120, 40);  // Set button position & size  

        // Adding event listener for button click
        button.addActionListener(new ActionListener() {  
            public void actionPerformed(ActionEvent e) {  
                JOptionPane.showMessageDialog(frame, "Button Clicked!");  
            }  
        });

        frame.add(button);  // Add button to frame  
        frame.setSize(300, 300);  // Set frame size  
        frame.setLayout(null);  
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);  
        frame.setVisible(true);  // Show frame  
    }  
}
