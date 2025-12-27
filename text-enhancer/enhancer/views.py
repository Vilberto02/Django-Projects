import os
from dotenv import load_dotenv
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from google import genai

load_dotenv()

class IAGenerateView(APIView):
  """
  Vista API para mejorar texto usando Gemini AI
  """
  
  def post(self, request, *args, **kwargs):
    try:
      user_text = request.data.get('texto', '')

      if not user_text:
        return Response(
          {"error": "Falta el texto"}, 
          status=status.HTTP_400_BAD_REQUEST
        )
      
      client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

      response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Mejora el siguiente texto: '{user_text}'"
      )

      return Response({
        "response": response.text,
        "status": "success"
      }, status=status.HTTP_200_OK)

    except Exception as e:
      return Response(
        {"error": str(e)}, 
        status=status.HTTP_500_INTERNAL_SERVER_ERROR
      )