using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerController : MonoBehaviour
{
    public float acceleration = 500f; // Forward force
    public float maxSpeed = 50f; // Speed limit
    public float turnSpeed = 100f; // Turning power
    public float driftFactor = 0.95f; // Drift control
    public float traction = 0.8f; // Grip factor

    private Rigidbody rb;
    private float moveInput;
    private float turnInput;

    void Start()
    {
        rb = GetComponent<Rigidbody>();
    }

    void FixedUpdate()
    {
        // Get player input
        moveInput = Input.GetAxis("Vertical");  // W/S or Up/Down Arrow
        turnInput = Input.GetAxis("Horizontal"); // A/D or Left/Right Arrow

        // Apply acceleration
        if (rb.linearVelocity.magnitude < maxSpeed)
        {
            rb.AddForce(transform.forward * moveInput * acceleration * Time.deltaTime, ForceMode.Acceleration);
        }

        // Apply turning
        if (Mathf.Abs(turnInput) > 0.1f)
        {
            rb.AddTorque(Vector3.up * turnInput * turnSpeed * Time.deltaTime, ForceMode.VelocityChange);
        }

        // Simulate drifting by adjusting sideways friction
        DriftControl();
    }

    void DriftControl()
    {
        Vector3 forwardVelocity = transform.forward * Vector3.Dot(rb.linearVelocity, transform.forward);
        Vector3 rightVelocity = transform.right * Vector3.Dot(rb.linearVelocity, transform.right);

        // Reduce sideways movement to simulate drift
        rb.linearVelocity = forwardVelocity + rightVelocity * driftFactor;
    }
}
