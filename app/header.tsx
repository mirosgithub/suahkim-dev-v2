'use client'
import { TextEffect } from '@/components/ui/text-effect'
import { Magnetic } from '@/components/ui/magnetic'
import Link from 'next/link'
import Image from 'next/image'
import { useTheme } from 'next-themes'
import { useEffect, useState } from 'react'

export function Header() {
  const { theme, systemTheme } = useTheme()
  const [mounted, setMounted] = useState(false)

  useEffect(() => {
    setMounted(true)
  }, [])

  if (!mounted) {
    return (
      <header className="mb-8 flex items-center justify-between">
        <div>
          <Magnetic springOptions={{ bounce: 0 }} intensity={0.3}>
            <Link href="/" className="font-medium text-black dark:text-white block">
              Suah Kim
            </Link>
          </Magnetic>
          <TextEffect
            as="p"
            preset="fade"
            per="char"
            className="text-zinc-600 dark:text-zinc-500"
            delay={0.5}
          >
            Intern @AKA | Part 3 Software Engineering @UoA
          </TextEffect>
        </div>
      </header>
    )
  }

  const currentTheme = theme === 'system' ? (systemTheme || 'light') : theme
  const logoSrc = currentTheme === 'dark' ? '/logo_dark.png' : '/logo.png'

  return (
    <header className="mb-8 flex items-center justify-between">
      <div>
        <Magnetic springOptions={{ bounce: 0 }} intensity={0.3}>
          <Link href="/" className="block mb-2">
            <Image
              src={logoSrc}
              alt="Suah Kim"
              width={56}
              height={56}
              className="h-14 w-14 object-contain"
              priority
            />
          </Link>
        </Magnetic>
        <Magnetic springOptions={{ bounce: 0 }} intensity={0.3}>
          <Link href="/" className="font-medium text-black dark:text-white block">
            Suah Kim
          </Link>
        </Magnetic>
        <TextEffect
          as="p"
          preset="fade"
          per="char"
          className="text-zinc-600 dark:text-zinc-500"
          delay={0.5}
        >
          Intern @AKA | Part 3 Software Engineering @UoA
        </TextEffect>
      </div>
    </header>
  )
}
