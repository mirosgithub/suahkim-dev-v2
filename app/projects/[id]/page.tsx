import Link from 'next/link'
import { PROJECTS } from '@/app/data'
import { Magnetic } from '@/components/ui/magnetic'

export default async function ProjectPage({
  params,
}: {
  params: Promise<{ id: string }>
}) {
  const { id } = await params
  const project = PROJECTS.find((p) => p.id === id)

  if (!project) {
    return (
      <div className="mx-auto max-w-4xl px-4 py-20">
        <Magnetic springOptions={{ bounce: 0 }} intensity={0.3}>
          <Link
            href="/"
            aria-label="Back to home"
            className="mb-8 inline-block text-zinc-600 transition-colors hover:text-zinc-900 dark:text-zinc-400 dark:hover:text-zinc-100"
          >
            ←
          </Link>
        </Magnetic>
        <div className="text-zinc-600 dark:text-zinc-400">Project not found.</div>
      </div>
    )
  }

  return (
    <div className="mx-auto max-w-4xl px-4 py-20">
      <Magnetic springOptions={{ bounce: 0 }} intensity={0.3}>
        <Link
          href="/"
          aria-label="Back to home"
          className="mb-8 inline-block text-zinc-600 transition-colors hover:text-zinc-900 dark:text-zinc-400 dark:hover:text-zinc-100"
        >
          ←
        </Link>
      </Magnetic>

      <h1 className="mb-4 text-3xl font-medium text-zinc-900 dark:text-zinc-50">
        {project.name}
      </h1>

      {project.description && (
        <>
          <p className="mb-10 text-zinc-600 dark:text-zinc-400">
            {project.description}
          </p>
          <br />
        </>
      )}

      {(project.demoUrl || project.githubUrl) && (
        <div className="mb-8 flex flex-wrap items-center gap-3">
          {project.demoUrl && (
            <Magnetic springOptions={{ bounce: 0 }} intensity={0.3}>
              <a
                href={project.demoUrl}
                target="_blank"
                rel="noopener noreferrer"
                className="group relative inline-flex shrink-0 items-center gap-[1px] rounded-full px-2.5 py-1 text-sm text-black transition-colors duration-200 hover:text-zinc-600 dark:text-zinc-100 dark:hover:text-zinc-300"
                data-id={project.demoUrl}
              >
                Live Demo
                <svg
                  width="15"
                  height="15"
                  viewBox="0 0 15 15"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                  className="h-3 w-3"
                >
                  <path
                    d="M3.64645 11.3536C3.45118 11.1583 3.45118 10.8417 3.64645 10.6465L10.2929 4L6 4C5.72386 4 5.5 3.77614 5.5 3.5C5.5 3.22386 5.72386 3 6 3L11.5 3C11.6326 3 11.7598 3.05268 11.8536 3.14645C11.9473 3.24022 12 3.36739 12 3.5L12 9.00001C12 9.27615 11.7761 9.50001 11.5 9.50001C11.2239 9.50001 11 9.27615 11 9.00001V4.70711L4.35355 11.3536C4.15829 11.5488 3.84171 11.5488 3.64645 11.3536Z"
                    fill="currentColor"
                    fillRule="evenodd"
                    clipRule="evenodd"
                  ></path>
                </svg>
              </a>
            </Magnetic>
          )}
          {project.githubUrl && (
            <Magnetic springOptions={{ bounce: 0 }} intensity={0.3}>
              <a
                href={project.githubUrl}
                target="_blank"
                rel="noopener noreferrer"
                className="group relative inline-flex shrink-0 items-center gap-[1px] rounded-full px-2.5 py-1 text-sm text-black transition-colors duration-200 hover:text-zinc-600 dark:text-zinc-100 dark:hover:text-zinc-300"
                data-id={project.githubUrl}
              >
                GitHub
                <svg
                  width="15"
                  height="15"
                  viewBox="0 0 15 15"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                  className="h-3 w-3"
                >
                  <path
                    d="M3.64645 11.3536C3.45118 11.1583 3.45118 10.8417 3.64645 10.6465L10.2929 4L6 4C5.72386 4 5.5 3.77614 5.5 3.5C5.5 3.22386 5.72386 3 6 3L11.5 3C11.6326 3 11.7598 3.05268 11.8536 3.14645C11.9473 3.24022 12 3.36739 12 3.5L12 9.00001C12 9.27615 11.7761 9.50001 11.5 9.50001C11.2239 9.50001 11 9.27615 11 9.00001V4.70711L4.35355 11.3536C4.15829 11.5488 3.84171 11.5488 3.64645 11.3536Z"
                    fill="currentColor"
                    fillRule="evenodd"
                    clipRule="evenodd"
                  ></path>
                </svg>
              </a>
            </Magnetic>
          )}
        </div>
      )}

      <div className="space-y-8">
        {(project.image || project.video) && (
          <div className="rounded-2xl overflow-hidden">
            {project.image ? (
              <img
                src={project.image}
                alt={project.name}
                className="aspect-video w-full object-cover bg-zinc-100 dark:bg-zinc-900"
              />
            ) : project.video ? (
              <video
                src={project.video}
                autoPlay
                loop
                muted
                playsInline
                className="aspect-video w-full bg-zinc-100 dark:bg-zinc-900"
              />
            ) : null}
          </div>
        )}

        {project.details && (() => {
          const projectShortName = project.name.split(':')[0]?.trim() || project.name
          const headers = [
            `What is ${projectShortName}?`,
            'Why was it created?',
            'Any challenges?',
          ]
          return (
            <div className="prose prose-gray dark:prose-invert">
              {project.details.split('\n\n').map((paragraph, index) => (
                <div key={index} className="mb-6">
                  <h3 className="text-lg font-medium text-zinc-900 dark:text-zinc-50 mb-2 not-prose">
                    {headers[index]}
                  </h3>
                  <p className="text-zinc-600 dark:text-zinc-400 leading-relaxed">
                    {paragraph}
                  </p>
                </div>
              ))}
            </div>
          )
        })()}
      </div>

      {project.techStack && project.techStack.length > 0 && (
        <div className="mt-8 text-sm text-zinc-600 dark:text-zinc-400 whitespace-pre">
          <br />
          {project.techStack.map((tech, index, arr) => (
            <span key={tech}>
              #{tech}
              {index < arr.length - 1 && '    '}
            </span>
          ))}
        </div>
      )}
    </div>
  )
}

