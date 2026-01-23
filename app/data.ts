type Project = {
  name: string
  description: string
  link: string
  video?: string
  image?: string
  id: string
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
      'Project overview',
    link: '/projects/portfolio-v2',
    id: 'portfolio-v2',
  },
  {
    name: 'Emoji processor',
    description: 'Project overview',
    link: '/projects/emoji-processor',
    id: 'emoji-processor',
  },
  {
    name: 'Lullab.ai',
    description: 'Project overview',
    link: '/projects/lullab-ai',
    id: 'lullab-ai',
  },
]

export const WORK_EXPERIENCE: WorkExperience[] = [
  {
    company: 'AKA Intelligence',
    title: 'Software Engineering Intern',
    description: 'Implementing AI training data ingestion pipelines.',
    start: 'Dec 2025',
    end: 'Present',
    link: '',
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

export const BLOG_POSTS: BlogPost[] = [
  {
    title: 'BlogPost1',
    description: 'Description for BlogPost1',
    link: '/blog/blogpost1',
    uid: 'blog-1',
  },
  {
    title: 'BlogPost2',
    description:
      'Description for BlogPost2',
    link: '/blog/blogpost2',
    uid: 'blog-2',
  },
]

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
