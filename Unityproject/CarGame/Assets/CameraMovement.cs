using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class FollowPlayer : MonoBehaviour
{
    public GameObject player; // Assign car in Unity Inspector
    private Vector3 offset = new Vector3(0, 5, -15); // Adjust as needed

    void LateUpdate()
    {
        if (player != null) // Ensure the car is assigned
        {
            transform.position = player.transform.position + offset;
        }
    }
}