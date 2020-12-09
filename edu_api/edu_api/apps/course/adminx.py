import xadmin

from course.models import CourseCategory, Course, Teacher, CourseChapter, CourseLesson


class CourseCategoryAdmin(object):
    """课程分类表"""
    list_display = ["name"]


xadmin.site.register(CourseCategory, CourseCategoryAdmin)


class CourseAdmin(object):
    """课程信息表"""
    list_display = ["name", "status",
                    "course_category", "lessons", "pub_lessons",
                    "price", "teacher"]


xadmin.site.register(Course, CourseAdmin)


class TeacherAdmin(object):
    """讲师表"""
    list_display = ["name", "role", "title", "signature", "image", "brief"]


xadmin.site.register(Teacher, TeacherAdmin)


class CourseChapterAdmin(object):
    """章节表"""
    list_display = ["course", "chapter", "name", "summary", "pub_date"]


xadmin.site.register(CourseChapter, CourseChapterAdmin)


class CourseLessonAdmin(object):
    """课时表"""
    list_display = ["name", "section_type", "section_link", "duration", "pub_date", "course", "is_show_list"]


xadmin.site.register(CourseLesson, CourseLessonAdmin)
