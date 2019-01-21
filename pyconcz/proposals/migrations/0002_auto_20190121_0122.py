# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-21 00:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='talk',
            name='gdpr_consent',
            field=models.BooleanField(default=False, verbose_name='I consent to storing data TODO'),
        ),
        migrations.AddField(
            model_name='workshop',
            name='gdpr_consent',
            field=models.BooleanField(default=False, verbose_name='I consent to storing data TODO'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='abstract',
            field=models.TextField(help_text='Try to write as if you’re talking to a real person.\nUse plain text or Markdown.\n\nYou might want to follow these guidelines:\nFirst introduce the problem your talk will bring a solution to.\nThen explain why it’s a problem worth solving.\nUse the last paragraph to tell your audience what is your approach to solving it.', verbose_name='Tell the audience more about your talk in 1–3 paragraphs (90–200 words total)'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='bio',
            field=models.TextField(help_text='Tell your audience in first person (e.g. „I write…“ not „Alex writes…“ ) about anything relevant about you, whether it’s your background, education, experience, current or former employer, hobbies or opensource software you maintain.\nYou can of course include anything fun or quirky about yourself.', verbose_name='Why are you the right person to talk about the topic you chose? (between 50 and 90 words)'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='difficulty',
            field=models.CharField(choices=[('beginner', 'Beginner  (suitable for everyone)'), ('advanced', 'Advanced  (requires a higher level of Python knowledge)')], default='beginner', max_length=10, verbose_name='Talk difficulty'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='email',
            field=models.EmailField(help_text='We’ll keep it secret and use only to contact you.', max_length=254, verbose_name='Your email address'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='full_name',
            field=models.CharField(help_text='Use a name that you’re comfortable with, or a nickname.\nFeel free to use Unicode characters.', max_length=200, verbose_name='What’s your name?'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='github',
            field=models.CharField(blank=True, help_text='Optional. The whole URL.', max_length=255, verbose_name='Your public code repository (GitHub, GitLab, …)'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='language',
            field=models.CharField(choices=[('en', 'English (preferred at PyCon CZ)'), ('cs', 'Czech or Slovak')], default='en', help_text='English is preferred, but if you feel uncomfortable with it, you can give your talk in Czech or Slovak', max_length=2, verbose_name='Talk language'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='needs_finaid',
            field=models.BooleanField(default=False, help_text='Covering travel or accommodation costs etc.\nPlease specify this here and now, otherwise we might not be able to grant you the aid.', verbose_name='I need financial aid to make this talk possible'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='photo',
            field=models.ImageField(help_text='If you don’t have a photo according to specs below, we will ask you for one if your talk is selected.\nIdeal photo is:\n– as large as possible (128 × 128 px, there is no upper limit, even 1000 × 1000 px isn’t too much),\n– as uncompressed as possible (JPEGs are ok),\n– doesn’t show other people\n– is a head shot (not you in front of a pyramid)\n– and has no “creative filters” applied.\nWe might crop it and change contrast, brightness etc. to fit PyCon CZ visual style.', upload_to='proposals/pyconcz2019/talks/', verbose_name='Your photo (not an\xa0illustration nor\xa0avatar)'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='referral_link',
            field=models.URLField(blank=True, default='', help_text='If you have a link to a publicly available recording of you giving a talk or leading a workshop, you can paste the link here. \nWill be used in the decision process.', verbose_name='Got a video?'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='title',
            field=models.CharField(help_text='The shortest way to say what it will be about.', max_length=200, verbose_name='Title of your talk'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='twitter',
            field=models.CharField(blank=True, help_text='Optional. Write it without the @.', max_length=255, verbose_name='Your Twitter handle'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='abstract',
            field=models.TextField(help_text='Try to write as if you’re talking to a real person.\nPlease include any requirements: hardware to bring (including laptops), libraries and Python version to be installed, expected experience with topics/libraries, etc.\nUse plain text or Markdown.', verbose_name='Tell the audience about your workshop or sprint in 1–3 paragraphs (90–200 words)'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='bio',
            field=models.TextField(help_text='Tell your audience in first person (e.g. „I write…“ not „Alex writes…“ ) about anything relevant about you, whether it’s your background, education, experience, current or former employer, hobbies or opensource software you maintain.\nYou can of course include anything fun or quirky about yourself.', verbose_name='Why are you the right person to lead a workshop about the topic you chose? (between 50 and 90 words)'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='difficulty',
            field=models.CharField(choices=[('beginner', 'Beginner  (suitable for everyone)'), ('advanced', 'Advanced  (requires a higher level of Python knowledge)')], default='beginner', max_length=10, verbose_name='Workshop difficulty'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='email',
            field=models.EmailField(help_text='We’ll keep it secret and use only to contact you.', max_length=254, verbose_name='Your email address'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='finaid_details',
            field=models.TextField(blank=True, help_text='Please state explicitly:\n1) why you need it,\n2) what for and\n3) how much in EUR or CZK.\nIf you require aid for more items (accommodation, travel costs etc.) please state the amount for each item.', null=True, verbose_name='Details about required financial aid'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='full_name',
            field=models.CharField(help_text='Use a name that you’re comfortable with, or a nickname.\nFeel free to use Unicode characters.', max_length=200, verbose_name='What’s your name?'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='github',
            field=models.CharField(blank=True, help_text='Optional. The whole URL.', max_length=255, verbose_name='Your public code repository (GitHub, GitLab, …)'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='language',
            field=models.CharField(choices=[('en', 'English (preferred at PyCon CZ)'), ('cs', 'Czech or Slovak')], default='en', help_text='English is preferred, but if you feel uncomfortable with it, you can hold your workshop in Czech or Slovak', max_length=2, verbose_name='Workshop or sprint language'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='needs_finaid',
            field=models.BooleanField(default=False, help_text='Covering travel or accommodation costs etc.\nPlease specify this here and now, otherwise we might not be able to grant you the aid.', verbose_name='I need financial aid to make this workshop possible'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='photo',
            field=models.ImageField(help_text='If you don’t have a photo according to specs below, we will ask you for one if your workshop is selected.\nIdeal photo is:\n– as large as possible (128 × 128 px, there is no upper limit, even 1000 × 1000 px isn’t too much),\n– as uncompressed as possible (JPEGs are ok),\n– doesn’t show other people\n– is a head shot (not you in front of a pyramid)\n– and has no “creative filters” applied.\nWe might crop it and change contrast, brightness etc. to fit PyCon CZ visual style.', upload_to='proposals/pyconcz2019/talks/', verbose_name='Your photo (not an\xa0illustration nor\xa0avatar)'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='referral_link',
            field=models.URLField(blank=True, default='', help_text='If you have a link to a publicly available recording of you giving a talk or leading a workshop, you can paste the link here. Will be used in the decision process.', verbose_name='Got a video?'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='requirements',
            field=models.TextField(blank=True, help_text='Do you have any special requirements that you expect us to fullfill?\nDo you need anything more than a room with chairs, desks, wifi, standard euro sockets and a projector?', null=True, verbose_name='Extra requirements'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='title',
            field=models.CharField(help_text='The shortest way to say what it will be about.', max_length=200, verbose_name='What is the title of your workshop or sprint?'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='twitter',
            field=models.CharField(blank=True, help_text='Optional. Write it without the @.', max_length=255, verbose_name='Your Twitter handle'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='type',
            field=models.CharField(choices=[('workshop', 'Workshop'), ('sprint', 'Sprint')], default='workshop', help_text='At a workshop, you should present hands-on exercises for participants to learn from. You’ll have a room and a limited number of participants.\nAt a sprint, participants help an open-source project – usually by cloning the repo and trying to fix beginner-level issues, while you’ll provide one-to-one mentorship. If several experienced developers are around, sprints are also a good place for serious design discussions. Sprinters only need a table to sit around, reliable wifi and dedication to do great things!', max_length=10, verbose_name='Choose a type'),
        ),
    ]
