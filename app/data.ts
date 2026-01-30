type Project = {
  name: string
  description: string
  link: string
  id: string
  details?: string
  githubUrl?: string
  demoUrl?: string
  techStack?: string[]
}

type WorkExperience = {
  company: string
  title: string
  description: string
  start: string
  end: string
  link: string
  id: string
}

type BlogPost = {
  title: string
  description: string
  link: string
  uid: string
}

type SocialLink = {
  label: string
  link: string
}

export const PROJECTS: Project[] = [
  {
    name: 'Portfolio website v.2',
    description:
      'My redesigned personal portfolio, migrated from Reflex to Next.js for improved frontend functionalities and cost effective deployment.',
    link: '/projects/portfolio-v2',
    id: 'portfolio-v2',
    githubUrl: 'https://github.com/mirosgithub/suahkim-dev-v2',
    techStack: ['Next.js', 'TypeScript', 'TailwindCSS', 'Vercel'],
    details:
      'This is a personal website to showcase my work and ideas with project demos and blog posts. I aim to update it as often as possible so the content will be most up-to-date. It is an ongoing project with new features coming up, so stay tuned!\n\nThe first version (version 1 in Flask, my first web app) was developed and deployed in July 2025. I used plain HTML/CSS for the frontend, and struggled with contact form spamming issues. It required manual deployment every time I update the structure and I wanted to try out modern UI/UX in React-based web apps, so I decided to redesign the website in version 2.\n\nInitially I chose Reflex to transition to React-based web development. It was straightforward to learn as it was Python-based, but lacked UI components, functionality and deployment support. As a result, I often had to rely on trial and error or wrap custom React components, which undermined the reason for choosing Reflex. Eventually I moved to Next.js, which provides easy deployment, custom domain support, automatic CI/CD and extensive UI library resources.',
  },
  {
    name: 'Emoji processor',
    description:
      'Python script using OpenCV to extract emojis from PNG sheets, handling inconsistent sizing and alignment through image detection.',
    link: '/projects/emoji-processor',
    id: 'emoji-processor',
    githubUrl: 'https://github.com/mirosgithub/emoji-processor',
    techStack: ['Python', 'OpenCV'],
    details:
      'The Python script extracts emojis from misaligned sprite sheets and removes backgrounds. It handles different sheet sizes and alignment through image detection rather than manual cropping, which provides a practical solution for batch-processing irregular image sources.\n\nI wanted to extract and process cute emojis from sprite sheets found on Pinterest to add them to my Notion workspace. Given the volume of emojis required, manual extraction would have been impractical.\n\nAll sprite sheets had different numbers of rows and columns with irregular spacing and alignment, so it was difficult to crop at the right place. Initially, I named the sheets `colourtheme_rows_cols` to calculate approximate dimensions of each emoji, which only worked on some sheets. The background removal also did not work well on lighter colours, so I switched to OpenCV to detect image edges, which made the script work for any emoji colour and layout.',
  },
  {
    name: 'Lullab.ai: Bedtime Story Generator',
    description:
      '1st place winner at WDCC x SESA Hackathon. Flask backend with Gemini API integration. Dockerised and deployed on Google Cloud Run.',
    link: '/projects/lullab-ai',
    id: 'lullab-ai',
    githubUrl: 'https://github.com/mirosgithub/lullabai',
    demoUrl: 'https://lullab-ai-713855574593.asia-southeast1.run.app/',
    techStack: ['Python', 'Flask', 'GoogleAPIs', 'Docker', 'GoogleCloudRun'],
    details: 'Lullab.ai creates and narrates custom bedtime stories for both children and adults. Users can input their name, keywords and their reasons for insomnia to generate unique and calming stories.\n\nIt was developed during the August 2025 WDCC x SESA Hackathon. The theme was Nostalgia, and our initial concept overlapped with two other teams.  Halfway through day one, we pivoted to creating nostalgic bedtime stories from childhood into comforting experiences for all ages.\n\nOur team had limited programming experience so I took charge of backend development. This challenge led me to develop and deploy my first AI-integrated application at my first hackathon with a team I met on the day.  Despite the difficulties, we achieved first place at the largest tertiary hackathon in NZ!',
  },
]

export const WORK_EXPERIENCE: WorkExperience[] = [
  {
    company: 'AKA Intelligence',
    title: 'Software Engineering Intern',
    description: 'Implementing AI training data ingestion pipelines.',
    start: 'Dec 2025',
    end: 'Present',
    link: 'https://www.akaintelligence.com/',
    id: 'aka-intelligence',
  },
  {
    company: 'Private Tutoring',
    title: 'Programming Tutor',
    description: 'Teaching MATLAB and C programming for first-year engineering students.',
    start: 'Nov 2025',
    end: 'Present',
    link: '',
    id: 'Programming-tutor',
  },
]

export const BLOG_POSTS: BlogPost[] = []

export const SOCIAL_LINKS: SocialLink[] = [
  {
    label: 'GitHub',
    link: 'https://github.com/mirosgithub',
  },
  {
    label: 'LinkedIn',
    link: 'https://linkedin.com/in/suah-adela-kim',
  },
]
