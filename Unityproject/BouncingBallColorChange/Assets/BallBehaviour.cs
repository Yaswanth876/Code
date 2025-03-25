using UnityEngine;

public class BallBehavior : MonoBehaviour
{
    private Renderer ballRenderer;

    void Start()
    {
        ballRenderer = GetComponent<Renderer>();
    }

    void OnCollisionEnter(Collision collision)
    {
        if (collision.gameObject.name == "Ground")
        {
            ChangeColor();
        }
    }

    void ChangeColor()
    {
        ballRenderer.material.color = new Color(Random.value, Random.value, Random.value);
    }
}
