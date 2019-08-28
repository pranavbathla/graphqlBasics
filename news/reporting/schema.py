import graphene
from graphene_django import DjangoObjectType

from .models import Reporter, Article


class ReporterType(DjangoObjectType):
    class Meta:
        model = Reporter


class ArticleType(DjangoObjectType):
    class Meta:
        model = Article


class Query(graphene.ObjectType):
    reporters = graphene.List(ReporterType)
    articles = graphene.List(ArticleType)

    def resolve_reporters(self, info, **kwargs):
        return Reporter.objects.all()

    def resolve_articles(self, info, **kwargs):
        return Article.objects.all()

class ReporterInput(graphene.InputObjectType):
    first_name = graphene.String()
    last_name = graphene.String()
    email = graphene.String()

class CreateReporter(graphene.Mutation):
    # id = graphene.Int()
    # first_name = graphene.String()
    # last_name = graphene.String()
    # email = graphene.String()
    reporter = graphene.Field(ReporterType)

    class Arguments:
        # first_name = graphene.String()
        # last_name = graphene.String()
        # email = graphene.String()
        reporter = ReporterInput()

    def mutate(self, info, reporter):
        first_name = reporter.first_name
        last_name = reporter.last_name
        email = reporter.email
        reporter = Reporter(first_name=first_name, last_name=last_name, email=email)
        reporter.save()

        # return CreateReporter(
        #     id=reporter.id,
        #     first_name=reporter.first_name,
        #     last_name=reporter.last_name,
        #     email=reporter.email
        # )
        return CreateReporter(reporter=reporter)

class ArticleInput(graphene.InputObjectType):
    headline = graphene.String()
    pub_date = graphene.Date()
    reporter_id = graphene.Int()

class CreateArticle(graphene.Mutation):
    # id = graphene.Int()
    # headline = graphene.String()
    # # pub_date = graphene.types.datetime.Date()
    # pub_date = graphene.Date()
    # #reporter = graphene.ObjectType
    article = graphene.Field(ArticleType)
    class Arguments:
        article = ArticleInput()

    def mutate(self, info, article):
        headline = article.headline
        pub_date = article.pub_date
        reporter_id = article.reporter_id
        article = Article(headline=headline, pub_date=pub_date, reporter_id=reporter_id)
        article.save()

        return CreateArticle(article=article)


class Mutation(graphene.ObjectType):
    create_reporter = CreateReporter.Field()
    create_article = CreateArticle.Field()

