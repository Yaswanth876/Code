import React from 'react';
import { Github, Linkedin, Mail, ExternalLink } from 'lucide-react';

const Portfolio = () => {
  // Sample data - replace with your own
  const personalInfo = {
    name: "John Doe",
    title: "Full Stack Developer",
    bio: "Passionate developer with 5 years of experience building web applications. Specialized in React, Node.js, and cloud technologies.",
    email: "john.doe@example.com",
    github: "https://github.com/johndoe",
    linkedin: "https://linkedin.com/in/johndoe"
  };

  const projects = [
    {
      title: "E-commerce Platform",
      description: "Built a full-stack e-commerce platform using React, Node.js, and MongoDB. Implemented features like user authentication, shopping cart, and payment processing.",
      technologies: ["React", "Node.js", "MongoDB", "Stripe"],
      link: "https://project1.com"
    },
    {
      title: "Task Management App",
      description: "Developed a collaborative task management application with real-time updates using Socket.io and React.",
      technologies: ["React", "Socket.io", "Express", "PostgreSQL"],
      link: "https://project2.com"
    },
    {
      title: "Weather Dashboard",
      description: "Created a weather dashboard that displays current and forecasted weather data using OpenWeather API.",
      technologies: ["React", "Redux", "OpenWeather API"],
      link: "https://project3.com"
    }
  ];

  const skills = [
    "JavaScript", "React", "Node.js", "Python",
    "SQL", "MongoDB", "AWS", "Docker",
    "Git", "TypeScript", "HTML/CSS", "Redux"
  ];

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header/Hero Section */}
      <header className="bg-white shadow-sm">
        <div className="max-w-4xl mx-auto px-4 py-16">
          <h1 className="text-4xl font-bold text-gray-900">{personalInfo.name}</h1>
          <p className="text-xl text-gray-600 mt-2">{personalInfo.title}</p>
          <p className="mt-4 text-gray-600 max-w-2xl">{personalInfo.bio}</p>
          
          <div className="flex gap-4 mt-6">
            <a href={personalInfo.github} className="text-gray-600 hover:text-gray-900">
              <Github className="w-6 h-6" />
            </a>
            <a href={personalInfo.linkedin} className="text-gray-600 hover:text-gray-900">
              <Linkedin className="w-6 h-6" />
            </a>
            <a href={`mailto:${personalInfo.email}`} className="text-gray-600 hover:text-gray-900">
              <Mail className="w-6 h-6" />
            </a>
          </div>
        </div>
      </header>

      {/* Projects Section */}
      <section className="py-16 px-4">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-3xl font-bold text-gray-900 mb-8">Projects</h2>
          <div className="grid gap-8 md:grid-cols-2">
            {projects.map((project, index) => (
              <div key={index} className="bg-white p-6 rounded-lg shadow-sm">
                <h3 className="text-xl font-semibold text-gray-900">{project.title}</h3>
                <p className="mt-2 text-gray-600">{project.description}</p>
                <div className="mt-4 flex flex-wrap gap-2">
                  {project.technologies.map((tech, techIndex) => (
                    <span
                      key={techIndex}
                      className="px-3 py-1 bg-gray-100 text-gray-600 text-sm rounded-full"
                    >
                      {tech}
                    </span>
                  ))}
                </div>
                <a
                  href={project.link}
                  className="mt-4 inline-flex items-center text-blue-600 hover:text-blue-800"
                >
                  View Project <ExternalLink className="w-4 h-4 ml-1" />
                </a>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Skills Section */}
      <section className="bg-white py-16 px-4">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-3xl font-bold text-gray-900 mb-8">Skills</h2>
          <div className="flex flex-wrap gap-3">
            {skills.map((skill, index) => (
              <span
                key={index}
                className="px-4 py-2 bg-gray-100 text-gray-700 rounded-full"
              >
                {skill}
              </span>
            ))}
          </div>
        </div>
      </section>

      {/* Contact Section */}
      <section className="py-16 px-4">
        <div className="max-w-4xl mx-auto text-center">
          <h2 className="text-3xl font-bold text-gray-900 mb-4">Get in Touch</h2>
          <p className="text-gray-600 mb-6">
            I'm always open to new opportunities and interesting projects.
          </p>
          <a
            href={`mailto:${personalInfo.email}`}
            className="inline-flex items-center px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
          >
            Contact Me <Mail className="w-4 h-4 ml-2" />
          </a>
        </div>
      </section>
    </div>
  );
};

export default Portfolio;